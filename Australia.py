from Samples.mapapi_PG import show_map


def show_maps():
    map_locations = {
        "Австралия": ("ll=135.746181,-27.483765&spn=20,20", "sat")
    }
    for map_location, map_type in map_locations.values():
        show_map(map_location, map_type)


def main():
    show_maps()


if __name__ == "__main__":
    main()