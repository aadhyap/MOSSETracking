from mosse import MOSSE
import argparse


if __name__ == '__main__':

	parse = argparse.ArgumentParser()
	parse.add_argument('--videopath', type=str, default='walking_AdobeExpress.mp4', help='walking video')
	parse.add_argument('--framepath', type=str, default='./videoData/walking/', help='frame path')
	args= parse.parse_args()
	tracker = MOSSE(args)
	#tracker.tracking()

    