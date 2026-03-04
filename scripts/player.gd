extends CharacterBody2D

signal died

@export var speed: float = 220.0
@export var jump_velocity: float = -420.0
@export var gravity_scale: float = 1.0
@export var max_hp: int = 5
@export var attack_damage: int = 1

var hp: int
var facing: int = 1
var attack_active := false

@onready var attack_area: Area2D = $AttackArea
@onready var attack_shape: CollisionShape2D = $AttackArea/CollisionShape2D

func _ready() -> void:
	hp = max_hp
	attack_shape.disabled = true

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity.y += ProjectSettings.get_setting("physics/2d/default_gravity") * gravity_scale * delta

	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = jump_velocity

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
	hp -= amount
	if hp <= 0:
		die()

func die() -> void:
	emit_signal("died")
