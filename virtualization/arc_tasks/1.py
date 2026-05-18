import os
import sys
try:
	import onnx
except Exception:
	onnx = None


def list_models(submission_dir):
	if not os.path.isdir(submission_dir):
		return []
	return [f for f in os.listdir(submission_dir) if f.lower().endswith('.onnx')]


def load_model(path):
	if onnx is None:
		raise RuntimeError('onnx package not available; install with `pip install onnx`')
	return onnx.load(path)


def main(argv=None):
	argv = argv or sys.argv[1:]
	base = os.path.dirname(__file__)
	submission_dir = os.path.join(base, 'submission')

	models = list_models(submission_dir)
	if not models:
		print('No .onnx models found in', submission_dir)
		return 1

	chosen = None
	if argv:
		# allow passing a filename or task id
		candidate = argv[0]
		if os.path.isfile(candidate):
			chosen = candidate
		else:
			# match by basename
			for m in models:
				if candidate.lower() in m.lower():
					chosen = os.path.join(submission_dir, m)
					break

	if chosen is None:
		if len(models) == 1:
			chosen = os.path.join(submission_dir, models[0])
		else:
			print('Multiple .onnx models found:')
			for i, m in enumerate(models, 1):
				print(f"  {i}. {m}")
			print('Pass the filename or task id as argument to load a specific model.')
			return 1

	try:
		model = load_model(chosen)
		print('Model loaded successfully:', chosen)
	except Exception as e:
		print('Failed to load model:', chosen)
		print('Error:', e)
		return 2

	return 0


if __name__ == '__main__':
	sys.exit(main())