extends Node

var death_count: int = 0

@onready var main := get_parent()
@onready var player := main.get_node("Player")
@onready var spawn_point := main.get_node("SpawnPoint")

func _ready() -> void:
	if player.has_signal("died"):
		player.died.connect(_on_player_died)

func _on_player_died() -> void:
	death_count += 1
	player.global_position = spawn_point.global_position
	player.velocity = Vector2.ZERO
	print("Deaths:", death_count)
