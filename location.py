from line_of_sight_map import LineOfSightMap
from highlight_peaks import HighlightPeaks


def test_location():
    # home
    # x = 306300.6
    # y = 671820.12
    # castle
    x = 279093
    y = 693777
    print("{0}, {1}".format(x, y))

    map = LineOfSightMap(x, y, None)
    map.create_map()
    print("created map")
    map.create_image()
    print("created image")

    peak_finder = HighlightPeaks()
    peaks = peak_finder.get_visible_peaks(map, x, y, map.observation_height)
    save_to_file(peaks)
    print("written peaks")


def save_to_file(peaks):
    with open("peaks.json", "w") as peaks_file:
        peaks_file.write("{\"peaks\":[")
        first = True
        for peak in peaks:
            if not first:
                peaks_file.write(",\n")
            line = \
                """
                    {{\"bearing\": {0},
                    \"elevation\": {1},
                    \"distance\": {2},
                    \"name\": \"{3}\",
                    \"height\": {4},
                    \"visible\": {5}}}
                """.format(peak.bearing, peak.elevation, peak.distance, peak.name, peak.height,
                           "true" if peak.visible else "false")
            peaks_file.write(line)
            first = False
        peaks_file.write("]}")


if __name__ == "__main__":
    test_location()
