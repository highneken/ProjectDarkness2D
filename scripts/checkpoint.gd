extends Area2D

signal activated(pos: Vector2)

var is_active := false

@onready var visual: ColorRect = $ColorRect

func _on_body_entered(body: Node2D) -> void:
	if body.name != "Player":
		return

	if not is_active:
		is_active = true
		visual.color = Color(0.95, 0.75, 0.25, 1)
		var tw := create_tween()
		tw.tween_property(visual, "scale", Vector2(1.25, 1.25), 0.12)
		tw.tween_property(visual, "scale", Vector2.ONE, 0.16)
		emit_signal("activated", global_position)

	if "hp" in body and "max_hp" in body:
		body.hp = body.max_hp
		if body.has_signal("hp_changed"):
			body.emit_signal("hp_changed", body.hp, body.max_hp)
