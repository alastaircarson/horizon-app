from line_of_sight_map import LineOfSightMap
from highlight_peaks import HighlightPeaks
from s3_service import S3Service
from io import BytesIO
from viewpoint import Viewpoint


def test_location():
    # castle
    x = 279093
    y = 693777
    print("{0}, {1}".format(x, y))

    viewpoints = Viewpoint()

    entries = viewpoints.get_unprocessed_viewpoints()

    print(entries)

    viewpoints.set_viewpoint_as_processed(entries[0]["id"], "test.png", "test.json")

#    map = LineOfSightMap(x, y, None)
#    map.create_map()
#    print("created map")
#    map.create_image()
#    print("created image")

#    peak_finder = HighlightPeaks()
#    peaks = peak_finder.get_visible_peaks(map, x, y, map.observation_height)
#    save_to_file(peaks)
#    print("written peaks")

#    s3_service = S3Service()
#    buffer = s3_service.download_binary_file("tw-foss4g-data", "data/hp/HP40.bin")
#    print(len(buffer.getvalue()))
#    upload = BytesIO(buffer.getvalue())
#    s3_service.upload_binary_file("tw-foss4g-data", "data/hp/test.bin", upload)


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
