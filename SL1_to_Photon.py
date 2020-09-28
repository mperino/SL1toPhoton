import glob
import os
import sys
import zipfile
import tempfile
import argparse
import pyphotonfile
from PIL import Image
# from IPython import embed

class SL1Reader:
    def __init__(self, filepath):
        self.zf = zipfile.ZipFile(filepath, 'r')
        self._read_config()
        self.n_layers = 0
        for filename in self.zf.namelist():
            if os.path.dirname(filename) is not '':  # skip all files in subdirectorys (e.g. thumbnails)
                continue
            if ".png" in filename:
                self.n_layers += 1

    def _read_config(self):
        try:
            config = self.zf.read('config.ini')
        except KeyError:
            print('ERROR: Did not find config.ini in zipped sl1 file')
        else:
            self.config = {}
            for line in config.decode().splitlines():
                key, value = line.strip().split('=')
                self.config[key.strip()] = value.strip()
        try:
            prusaslicer = self.zf.read('prusaslicer.ini')
        except KeyError:
            print('ERROR: Did not find prusaslicer in zipped sl1 file')
        else:
            self.prusaslicer = {}
            for line in prusaslicer.decode().splitlines():
                key, value = line.strip().split('=',1)
                self.prusaslicer[key.strip()] = value.strip()

    def extract_images(self, dirpath):
        try:
            os.makedirs(dirpath)
        except OSError:
            pass
        for filename in self.zf.namelist():
            if os.path.dirname(filename) is not '':  # skip all files in subdirectorys (e.g. thumbnails)
                continue
            if ".png" in filename:
                data = self.zf.read(filename)
                with open(os.path.join(dirpath, filename), 'bw') as f:
                    f.write(data)

if __name__ == '__main__':
    desc = '''Convert an SL1 file to a Photon file.'''
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("sl1_file", help="SL1 file to convert.")
    parser.add_argument("-f", "--force", action='store_true', help="overwrite existing files.")
    # parser.add_argument("--timelapse", action='store_true', default=False, help="set all exposures to 1s. Useful for debugging exposure with no resin.")
    parser.add_argument("-v", "--verbose", action='store_true', default=False)
    parser.add_argument("-o", "--output", help="photon file output path.")
    args = parser.parse_args()
    # print(args)
    if args.output is None:
        base, ext = os.path.splitext(args.sl1_file)
        photon_path = base + '.photon'
    else:
        photon_path = args.output
    if os.path.exists(photon_path) and args.force is False:
        print('ERROR: file {} already exists!. move or use -f flag to force overwrite. Cancelling...'.format(os.path.basename(photon_path)))
        sys.exit(-1)

    sl1 = SL1Reader(args.sl1_file)
    photon = pyphotonfile.Photon()
    photon.exposure_time = float(sl1.config['expTime'])
    photon.exposure_time_bottom = float(sl1.config['expTimeFirst'])
    photon.layer_height = float(sl1.config['layerHeight'])
    photon.bottom_layers = int(sl1.config['numFade'])
# the try clause bellow is for importing settings from the prusaslicer.ini in the .sl1 file.
# Current logic is to bomb out if we cant find the bed size, but we could default back to 1440 by uncommenting and commenting out the exit
    try:
        photon.bed_x = int(sl1.prusaslicer['display_width'])
        photon.bed_y = int(sl1.prusaslicer['display_height'])
    except:
        print('ERROR: Unable to set display width or height from .sl1 file')
        # print ("setting a default size of 1440x2560")
        # photon.bed_x = 1440
        # photon.bed_y = 2560
        sys.exit(-1)

    if args.verbose:
        print('=== PARAMETERS ===')
        print('Exposure Time: {}'.format(photon.exposure_time))
        print('Bottom Exposure Time: {}'.format(photon.exposure_time_bottom))
        print('Layer Height: {}'.format(photon.layer_height))
        print('Bottom Layers: {}'.format(photon.bottom_layers))
        print('Layers: {}'.format(sl1.n_layers))
        print('Display X Width: {}'.format(photon.bed_x))
        print('Display Y Height: {}'.format(photon.bed_y))
        print('=== CONVERSION ===')
    with tempfile.TemporaryDirectory() as tmpdirname:
        if args.verbose:
            print('extracting layers... ', end='')
        sl1.extract_images(tmpdirname)
        if args.verbose:
            print('DONE')
        for i, filepath in enumerate(sorted(glob.glob(os.path.join(tmpdirname, '*.png')))):
            if args.verbose:
                print('converting layer {} / {} '.format(i+1, sl1.n_layers), end='')
            Image.open(filepath).rotate(180).save(filepath)
            photon.append_layer(filepath)
            if args.verbose:
                print('DONE')

    photon.write(photon_path)
    print('Output file written to: {}'.format(photon_path))

