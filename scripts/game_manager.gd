extends Node

signal death_count_changed(count: int)

var death_count: int = 0
const THRONE_ROOM := "res://scenes/ThroneRoom.tscn"

@onready var main := get_parent()
@onready var player := main.get_node("Player")
@onready var spawn_point := main.get_node("SpawnPoint")
@onready var vision := main.get_node_or_null("VisionOverlay")
var respawn_pos: Vector2

func _ready() -> void:
	respawn_pos = spawn_point.global_position
	
	# M1: Load persisted death count if available
	_load_persisted_death_count()
	
	if player.has_signal("died"):
		player.died.connect(_on_player_died)

	for checkpoint in get_tree().get_nodes_in_group("checkpoints"):
		if checkpoint.has_signal("activated"):
			checkpoint.activated.connect(_on_checkpoint_activated)

func _load_persisted_death_count() -> void:
	var tree := get_tree()
	if tree:
		var persist := tree.root.get_node_or_null("DeathPersist")
		if persist and persist.has_meta("death_count"):
			death_count = persist.get_meta("death_count")
			emit_signal("death_count_changed", death_count)

func _on_checkpoint_activated(pos: Vector2) -> void:
	# M1: Checkpoints only heal, respawn is always Throne Room (curse loop)
	print("Checkpoint healed player")

func _on_player_died() -> void:
	death_count += 1
	emit_signal("death_count_changed", death_count)
	
	# M1: Curse loop - always respawn in Throne Room
	# Store death count in a global or autoload for persistence across scenes
	var tree := get_tree()
	if tree:
		# Use a simple approach: store in an autoload or use a global approach
		# For now, we'll use a node in the root to persist death count
		var persist := tree.root.get_node_or_null("DeathPersist")
		if persist == null:
			persist = Node.new()
			persist.name = "DeathPersist"
			tree.root.add_child(persist)
		persist.set_meta("death_count", death_count)
		
		tree.change_scene_to_file(THRONE_ROOM)
	
	print("Deaths:", death_count, " - Returning to Throne Room")

func _load_persisted_death_count() -> void:
	var tree := get_tree()
	if tree:
		var persist := tree.root.get_node_or_null("DeathPersist")
		if persist and persist.has_meta("death_count"):
			death_count = persist.get_meta("death_count")
			emit_signal("death_count_changed", death_count)
