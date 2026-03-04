extends CanvasLayer

@onready var hp_label: Label = $Panel/HpLabel
@onready var death_label: Label = $Panel/DeathLabel
@onready var dash_label: Label = $Panel/DashLabel

var player_ref: Node

func _ready() -> void:
	var player := get_parent().get_node("Player")
	var gm := get_parent().get_node("GameManager")
	player_ref = player

	if player.has_signal("hp_changed"):
		player.hp_changed.connect(_on_hp_changed)
		_on_hp_changed(player.hp, player.max_hp)

	if gm.has_signal("death_count_changed"):
		gm.death_count_changed.connect(_on_death_count_changed)
		_on_death_count_changed(gm.death_count)

func _process(_delta: float) -> void:
	if player_ref == null:
		return
	if "dash_cooldown_left" in player_ref:
		var cd: float = player_ref.dash_cooldown_left
		if cd <= 0.01:
			dash_label.text = "Dash: READY"
		else:
			dash_label.text = "Dash: %.1fs" % cd

func _on_hp_changed(current: int, max_hp: int) -> void:
	hp_label.text = "HP: %d/%d" % [current, max_hp]

func _on_death_count_changed(count: int) -> void:
	death_label.text = "Deaths: %d" % count
