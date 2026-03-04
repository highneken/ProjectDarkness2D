extends CanvasLayer

@export_multiline var intro_text: String = ""

@onready var panel: Panel = $Panel
@onready var label: Label = $Panel/Label

func _ready() -> void:
	panel.visible = false
	if intro_text.strip_edges() != "":
		show_vision(intro_text, 3.2)

func show_vision(text: String, duration: float = 2.8) -> void:
	label.text = text
	panel.modulate.a = 0.0
	panel.visible = true
	var tw := create_tween()
	tw.tween_property(panel, "modulate:a", 1.0, 0.25)
	tw.tween_interval(duration)
	tw.tween_property(panel, "modulate:a", 0.0, 0.4)
	tw.tween_callback(func(): panel.visible = false)
