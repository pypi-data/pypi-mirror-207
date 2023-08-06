from easy_mitk import measure
from constant import Path


def test_surface_area():
    area = measure.surface_area(Path.NIfTI_MASK_CASE1)
    area = measure.surface_area('/app/workers/liver-worker/tmp/liver04.nii.gz')
    print(f'surface area of this mask: {area} cm^2')

def test_volume():
    volume = measure.volume(Path.NIfTI_MASK_CASE1)
    volume = measure.volume('/app/workers/liver-worker/tmp/liver04.nii.gz')
    print(f'volume of this mask: {volume} ml')


if __name__ == '__main__':
    test_surface_area()
    test_volume()
