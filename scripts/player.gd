extends CharacterBody2D

signal died
signal hp_changed(current: int, max: int)

@export var speed: float = 220.0
@export var jump_velocity: float = -420.0
@export var gravity_scale: float = 1.0
@export var max_hp: int = 5
@export var attack_damage: int = 1
@export var coyote_time: float = 0.12
@export var jump_buffer_time: float = 0.12
@export var short_jump_cut: float = 0.5
@export var invuln_time: float = 0.6
@export var dash_speed: float = 520.0
@export var dash_time: float = 0.16
@export var dash_cooldown: float = 0.7
@export var use_custom_character_art: bool = true
@export var custom_character_texture: Texture2D = preload("res://assets/sprites/mc_main.png")
@export var custom_character_scale: Vector2 = Vector2(0.09, 0.09)

const FRAME_IDLE := Rect2(1169, 189, 82, 60)
const FRAME_WALK_1 := Rect2(842, 257, 82, 60)
const FRAME_WALK_2 := Rect2(926, 257, 82, 60)
const FRAME_JUMP := Rect2(1505, 189, 82, 60)
const FRAME_ATTACK_1 := Rect2(338, 257, 82, 60)
const FRAME_ATTACK_2 := Rect2(422, 257, 82, 60)

var hp: int
var facing: int = 1
var attack_active := false
var coyote_timer := 0.0
var jump_buffer_timer := 0.0
var invuln := false
var is_dashing := false
var dash_time_left := 0.0
var dash_cooldown_left := 0.0
var walk_anim_t := 0.0

@onready var attack_area: Area2D = $AttackArea
@onready var attack_shape: CollisionShape2D = $AttackArea/CollisionShape2D
@onready var body_visual: ColorRect = $ColorRect
@onready var body_shadow: Sprite2D = $BodyShadow
@onready var body_sprite: Sprite2D = $BodySprite
@onready var sword_visual: ColorRect = $Sword
@onready var slash_trail: ColorRect = $SlashTrail

var use_atlas_frames := true

func _apply_custom_character_art() -> void:
	if not use_custom_character_art or custom_character_texture == null:
		return
	body_sprite.texture = custom_character_texture
	body_sprite.region_enabled = false
	body_sprite.scale = custom_character_scale
	body_sprite.position = Vector2(0, -22)
	body_shadow.visible = false

func _ready() -> void:
	hp = max_hp
	attack_shape.disabled = true
	body_visual.visible = false
	sword_visual.visible = false
	slash_trail.visible = false
	_apply_custom_character_art()
	use_atlas_frames = body_sprite.region_enabled
	if use_atlas_frames:
		body_sprite.region_rect = FRAME_IDLE
		body_shadow.region_rect = FRAME_IDLE
	emit_signal("hp_changed", hp, max_hp)

func _physics_process(delta: float) -> void:
	dash_cooldown_left = max(dash_cooldown_left - delta, 0.0)

	if Input.is_action_just_pressed("dash") and dash_cooldown_left <= 0.0 and not is_dashing:
		is_dashing = true
		dash_time_left = dash_time
		dash_cooldown_left = dash_cooldown

	if is_dashing:
		dash_time_left -= delta
		velocity = Vector2(facing * dash_speed, 0)
		if dash_time_left <= 0.0:
			is_dashing = false
	else:
		if Input.is_action_just_pressed("jump"):
			jump_buffer_timer = jump_buffer_time
		else:
			jump_buffer_timer = max(jump_buffer_timer - delta, 0.0)

		if is_on_floor():
			coyote_timer = coyote_time
		else:
			coyote_timer = max(coyote_timer - delta, 0.0)
			velocity.y += ProjectSettings.get_setting("physics/2d/default_gravity") * gravity_scale * delta

		if jump_buffer_timer > 0.0 and coyote_timer > 0.0:
			velocity.y = jump_velocity
			jump_buffer_timer = 0.0
			coyote_timer = 0.0

		if Input.is_action_just_released("jump") and velocity.y < 0.0:
			velocity.y *= short_jump_cut

		var direction := Input.get_axis("move_left", "move_right")
		if direction != 0:
			velocity.x = direction * speed
			facing = 1 if direction > 0 else -1
		else:
			velocity.x = move_toward(velocity.x, 0, speed)

		if Input.is_action_just_pressed("attack") and not attack_active:
			start_attack()

	attack_area.position.x = 26 * facing
	sword_visual.position = Vector2(16 * facing, -8)
	slash_trail.position = Vector2(22 * facing, -12)
	sword_visual.scale.x = facing
	slash_trail.scale.x = facing
	body_sprite.flip_h = facing < 0
	move_and_slide()
	_update_visual_state(delta)
	body_shadow.flip_h = body_sprite.flip_h
	if use_atlas_frames:
		body_shadow.region_rect = body_sprite.region_rect

	if global_position.y > 1200:
		die()

func _update_visual_state(delta: float) -> void:
	if not use_atlas_frames:
		return
	if attack_active:
		return
	if not is_on_floor():
		body_sprite.region_rect = FRAME_JUMP
		return
	if abs(velocity.x) > 5.0:
		walk_anim_t += delta * 9.0
		body_sprite.region_rect = FRAME_WALK_1 if int(walk_anim_t) % 2 == 0 else FRAME_WALK_2
	else:
		body_sprite.region_rect = FRAME_IDLE

func start_attack() -> void:
	attack_active = true
	attack_shape.disabled = false
	if use_atlas_frames:
		body_sprite.region_rect = FRAME_ATTACK_1

	sword_visual.visible = true
	slash_trail.visible = true
	slash_trail.modulate.a = 0.0
	slash_trail.rotation = -0.45 * facing
	sword_visual.rotation = -0.25 * facing

	var tw := create_tween()
	tw.tween_property(slash_trail, "modulate:a", 0.8, 0.05)
	tw.parallel().tween_property(sword_visual, "rotation", 0.45 * facing, 0.09)
	if use_atlas_frames:
		tw.parallel().tween_callback(func(): body_sprite.region_rect = FRAME_ATTACK_2)
	tw.tween_property(slash_trail, "modulate:a", 0.0, 0.08)

	for body in attack_area.get_overlapping_bodies():
		if body.has_method("take_damage"):
			body.take_damage(attack_damage)

	await get_tree().create_timer(0.12).timeout
	attack_shape.disabled = true
	sword_visual.visible = false
	slash_trail.visible = false
	await get_tree().create_timer(0.14).timeout
	attack_active = false

func take_damage(amount: int) -> void:
	if invuln:
		return
	hp -= amount
	emit_signal("hp_changed", hp, max_hp)
	invuln = true
	
	# M1: Screenshake and hit feedback
	_trigger_screenshake()
	_flash_damage()
	
	await get_tree().create_timer(invuln_time).timeout
	body_sprite.modulate = Color(1, 1, 1, 1)
	invuln = false
	if hp <= 0:
		die()

func _trigger_screenshake() -> void:
	var camera := get_node_or_null("Camera2D")
	if camera:
		var tween := create_tween()
		for i in range(5):
			tween.tween_property(camera, "offset", Vector2(randf_range(-3, 3), randf_range(-3, 3)), 0.03)
		tween.tween_property(camera, "offset", Vector2.ZERO, 0.1)

func _flash_damage() -> void:
	body_sprite.modulate = Color(1, 0.3, 0.3, 1)

func die() -> void:
	emit_signal("died")
