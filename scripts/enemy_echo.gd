extends CharacterBody2D

@export var speed: float = 90.0
@export var gravity_scale: float = 1.0
@export var max_hp: int = 2
@export var contact_damage: int = 1
@export var patrol_distance: float = 120.0

var hp: int
var dir: int = 1
var start_x: float
var hit_cooldown := false

func _ready() -> void:
	hp = max_hp
	start_x = global_position.x

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity.y += ProjectSettings.get_setting("physics/2d/default_gravity") * gravity_scale * delta

	velocity.x = dir * speed
	if global_position.x > start_x + patrol_distance:
		dir = -1
	elif global_position.x < start_x - patrol_distance:
		dir = 1

	move_and_slide()

func take_damage(amount: int) -> void:
	hp -= amount
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
