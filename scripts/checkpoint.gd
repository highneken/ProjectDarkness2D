extends Area2D

signal activated(pos: Vector2)

var is_active := false

@onready var visual: ColorRect = $ColorRect

func _on_body_entered(body: Node2D) -> void:
	if is_active:
		return
	if body.name != "Player":
		return
	is_active = true
	visual.color = Color(0.95, 0.75, 0.25, 1)
	emit_signal("activated", global_position)
