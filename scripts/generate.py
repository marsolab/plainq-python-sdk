"""Regenerate protobuf and gRPC code from the checked-in schema."""
from pathlib import Path
from grpc_tools import protoc
import grpc_tools

root = Path(__file__).resolve().parents[1]
result = protoc.main([
    "grpc_tools.protoc", f"-Iplainq/v1={root / 'proto/v1'}",
    f"-I{Path(grpc_tools.__file__).parent / '_proto'}",
    f"--python_out={root / 'src'}", f"--pyi_out={root / 'src'}",
    f"--grpc_python_out={root / 'src'}", "plainq/v1/schema.proto",
])
raise SystemExit(result)
