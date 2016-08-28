test: venv2.5.0 venv2.6.1 venv3.0.0
	for libver in 2.5.0 2.6.1 3.0.0; do \
		for pb2ver in 2.5.0 2.6.1 3.0.0; do \
			echo === protoc $$pb2ver and python package $$libver; \
			(. "venv$$libver/bin/activate"; \
				PYTHONPATH=$$pb2ver python -m proto2_pb2); \
		done; \
	done
 
venv2.5.0:
	virtualenv "$@"
	(. "$@"/bin/activate; pip install protobuf==2.5.0)

venv2.6.1:
	virtualenv "$@"
	(. "$@"/bin/activate; pip install protobuf==2.6.1)

venv3.0.0:
	virtualenv "$@"
	(. "$@"/bin/activate; pip install protobuf==3.0.0)
