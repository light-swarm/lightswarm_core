
world_dimensions = [200, 200]

## april_detector calibration
sense_camera_points = np.float32(np.array([[0,  20, 180], [100,   20, 180], [0, 20, 280], [100, 20, 280]]))
sense_world_points = np.float32(np.array([[0, -100,  20], [100, -100,  20], [0,  0,  20], [100,  0,  20]]))

## for shadow computation
projector_locations = [('first', (100, 100, 500)), ('second', (-100, -100, 500))]

