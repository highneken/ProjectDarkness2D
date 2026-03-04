extends TileMap

const TILE := 16
const SOURCE_ID := 0

func _ready() -> void:
	var tileset := TileSet.new()
	var src := TileSetAtlasSource.new()
	src.texture = preload("res://assets/external/gothicvania/gothicvania_church/assets/environment/tileset.png")
	src.texture_region_size = Vector2i(TILE, TILE)

	for y in range(0, 6):
		for x in range(0, 12):
			src.create_tile(Vector2i(x, y))

	tileset.add_source(src, SOURCE_ID)
	tile_set = tileset
	clear()

	# Room2 ground band
	for x in range(-4, 84):
		set_cell(0, Vector2i(x, 40), SOURCE_ID, Vector2i((x % 6 + 6) % 6, 0))
		set_cell(0, Vector2i(x, 41), SOURCE_ID, Vector2i((x % 6 + 6) % 6, 1))
		set_cell(0, Vector2i(x, 42), SOURCE_ID, Vector2i((x % 6 + 6) % 6, 2))

	# Platform 1
	for x in range(23, 38):
		set_cell(0, Vector2i(x, 32), SOURCE_ID, Vector2i((x % 6 + 6) % 6, 0))
		set_cell(0, Vector2i(x, 33), SOURCE_ID, Vector2i((x % 6 + 6) % 6, 1))

	# Platform 2
	for x in range(45, 60):
		set_cell(0, Vector2i(x, 28), SOURCE_ID, Vector2i((x % 6 + 6) % 6, 0))
		set_cell(0, Vector2i(x, 29), SOURCE_ID, Vector2i((x % 6 + 6) % 6, 1))
