extends CharacterBody2D

signal died

@export var speed: float = 220.0
@export var jump_velocity: float = -420.0
@export var gravity_scale: float = 1.0
@export var max_hp: int = 5
@export var attack_damage: int = 1
@export var coyote_time: float = 0.12
@export var jump_buffer_time: float = 0.12
@export var short_jump_cut: float = 0.5
@export var invuln_time: float = 0.6

var hp: int
var facing: int = 1
var attack_active := false
var coyote_timer := 0.0
var jump_buffer_timer := 0.0
var invuln := false

@onready var attack_area: Area2D = $AttackArea
@onready var attack_shape: CollisionShape2D = $AttackArea/CollisionShape2D
@onready var body_visual: ColorRect = $ColorRect

func _ready() -> void:
	hp = max_hp
	attack_shape.disabled = true

func _physics_process(delta: float) -> void:
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
	move_and_slide()

	if global_position.y > 1200:
		die()

func start_attack() -> void:
	attack_active = true
	attack_shape.disabled = false
	for body in attack_area.get_overlapping_bodies():
		if body.has_method("take_damage"):
			body.take_damage(attack_damage)
	await get_tree().create_timer(0.12).timeout
	attack_shape.disabled = true
	await get_tree().create_timer(0.18).timeout
	attack_active = false

func take_damage(amount: int) -> void:
	if invuln:
		return
	hp -= amount
	invuln = true
	body_visual.color = Color(1, 0.45, 0.45, 1)
	await get_tree().create_timer(invuln_time).timeout
	body_visual.color = Color(0.8, 0.85, 0.95, 1)
	invuln = false
	if hp <= 0:
		die()

func die() -> void:
	emit_signal("died")
