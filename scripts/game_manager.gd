extends Node

signal death_count_changed(count: int)

const THRONE_ROOM := "res://scenes/ThroneRoom.tscn"
var death_count: int = 0

@onready var main := get_parent()
@onready var player := main.get_node_or_null("Player")

func _ready() -> void:
	_load_persisted_death_count()
	if player and player.has_signal("died"):
		player.died.connect(_on_player_died)
	emit_signal("death_count_changed", death_count)

func _on_player_died() -> void:
	death_count += 1
	_save_persisted_death_count()
	emit_signal("death_count_changed", death_count)
	get_tree().change_scene_to_file(THRONE_ROOM)

func _save_persisted_death_count() -> void:
	var tree := get_tree()
	if tree == null:
		return
	var persist := tree.root.get_node_or_null("DeathPersist")
	if persist == null:
		persist = Node.new()
		persist.name = "DeathPersist"
		tree.root.add_child(persist)
	persist.set_meta("death_count", death_count)

func _load_persisted_death_count() -> void:
	var tree := get_tree()
	if tree == null:
		return
	var persist := tree.root.get_node_or_null("DeathPersist")
	if persist and persist.has_meta("death_count"):
		death_count = int(persist.get_meta("death_count"))
