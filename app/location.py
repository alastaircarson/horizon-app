from line_of_sight_map import LineOfSightMap
from highlight_peaks import HighlightPeaks
from s3_service import S3Service
import os
from viewpoint import Viewpoint


def test_location():
    # castle
    x = 279093
    y = 693777
    print("{0}, {1}".format(x, y))

    viewpoints = Viewpoint()

    entries = viewpoints.get_unprocessed_viewpoints()

    print(entries)

    for entry in entries:

        # Generate the LineOfSight map
        map = LineOfSightMap(entry["x"], entry["y"], None)
        map.create_map()
        print("created map")

        # Create a Horizon image
        image_filename = f"image{entry['id']}.png"
        map.create_image(image_filename)
        print("created image")

        # Create a Peaks file
        peaks_filename = f"peaks{entry['id']}.json"
        peak_finder = HighlightPeaks()
        peaks = peak_finder.get_visible_peaks(map, entry["x"], entry["y"], map.observation_height)
        peak_finder.save_to_file(peaks, peaks_filename)
        print("written peaks")

        s3_service = S3Service()
        s3_service.upload_file("tw-foss4g-app", f"data/{image_filename}", image_filename)
        s3_service.make_file_public("tw-foss4g-app", f"data/{image_filename}")
        s3_service.upload_file("tw-foss4g-app", f"data/{peaks_filename}", peaks_filename)
        s3_service.make_file_public("tw-foss4g-app", f"data/{image_filename}")

        os.remove(image_filename)
        os.remove(peaks_filename)

        viewpoints.set_viewpoint_as_processed(entries[0]["id"], image_filename, peaks_filename)


if __name__ == "__main__":
    test_location()
