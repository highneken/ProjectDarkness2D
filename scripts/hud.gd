extends CanvasLayer

@onready var hp_label: Label = $Panel/HpLabel
@onready var death_label: Label = $Panel/DeathLabel

func _ready() -> void:
	var player := get_parent().get_node("Player")
	var gm := get_parent().get_node("GameManager")

	if player.has_signal("hp_changed"):
		player.hp_changed.connect(_on_hp_changed)
		_on_hp_changed(player.hp, player.max_hp)

	if gm.has_signal("death_count_changed"):
		gm.death_count_changed.connect(_on_death_count_changed)
		_on_death_count_changed(gm.death_count)

func _on_hp_changed(current: int, max_hp: int) -> void:
	hp_label.text = "HP: %d/%d" % [current, max_hp]

func _on_death_count_changed(count: int) -> void:
	death_label.text = "Deaths: %d" % count
