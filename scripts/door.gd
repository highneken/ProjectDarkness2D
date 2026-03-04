extends Area2D

@export_file("*.tscn") var target_scene: String = ""
@export var door_label: String = "Door"

@onready var label_node: Label = $Label

func _ready() -> void:
	label_node.text = door_label

func _on_body_entered(body: Node2D) -> void:
	if body.name != "Player":
		return
	if target_scene == "":
		return
	get_tree().change_scene_to_file(target_scene)
