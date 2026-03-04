extends Node

signal death_count_changed(count: int)

var death_count: int = 0

@onready var main := get_parent()
@onready var player := main.get_node("Player")
@onready var spawn_point := main.get_node("SpawnPoint")
var respawn_pos: Vector2

func _ready() -> void:
	respawn_pos = spawn_point.global_position
	if player.has_signal("died"):
		player.died.connect(_on_player_died)

	for checkpoint in get_tree().get_nodes_in_group("checkpoints"):
		if checkpoint.has_signal("activated"):
			checkpoint.activated.connect(_on_checkpoint_activated)

func _on_checkpoint_activated(pos: Vector2) -> void:
	respawn_pos = pos
	print("Checkpoint aktiviert:", respawn_pos)

func _on_player_died() -> void:
	death_count += 1
	player.global_position = respawn_pos
	player.velocity = Vector2.ZERO
	if "hp" in player and "max_hp" in player:
		player.hp = player.max_hp
		if player.has_signal("hp_changed"):
			player.emit_signal("hp_changed", player.hp, player.max_hp)
	emit_signal("death_count_changed", death_count)
	print("Deaths:", death_count)
