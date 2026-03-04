extends CharacterBody2D

@export var speed: float = 80.0
@export var chase_speed: float = 125.0
@export var gravity_scale: float = 1.0
@export var max_hp: int = 3
@export var contact_damage: int = 1
@export var patrol_distance: float = 120.0

var hp: int
var dir: int = 1
var start_x: float
var hit_cooldown := false
var target: Node2D

@onready var visual: ColorRect = $ColorRect

func _ready() -> void:
	hp = max_hp
	start_x = global_position.x

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity.y += ProjectSettings.get_setting("physics/2d/default_gravity") * gravity_scale * delta

	if is_instance_valid(target):
		var d: float = sign(target.global_position.x - global_position.x)
		if d == 0.0:
			d = float(dir)
		dir = int(d)
		velocity.x = dir * chase_speed
	else:
		velocity.x = dir * speed
		if global_position.x > start_x + patrol_distance:
			dir = -1
		elif global_position.x < start_x - patrol_distance:
			dir = 1

	move_and_slide()

func take_damage(amount: int) -> void:
	hp -= amount
	visual.color = Color(0.9, 0.45, 0.45, 1)
	await get_tree().create_timer(0.08).timeout
	visual.color = Color(0.45, 0.5, 0.55, 1)
	if hp <= 0:
		queue_free()

func _on_hitbox_body_entered(body: Node2D) -> void:
	if hit_cooldown:
		return
	if body.has_method("take_damage"):
		hit_cooldown = true
		body.take_damage(contact_damage)
		await get_tree().create_timer(0.6).timeout
		hit_cooldown = false

func _on_detection_area_body_entered(body: Node2D) -> void:
	if body.name == "Player":
		target = body

func _on_detection_area_body_exited(body: Node2D) -> void:
	if body == target:
		target = null
