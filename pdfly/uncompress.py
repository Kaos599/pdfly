# uncompress.py
"""Provides functionality to uncompress PDF files."""
from pathlib import Path
import zlib
from typing import cast

from pypdf import PdfReader, PdfWriter
from pypdf.generic import IndirectObject, StreamObject


def main(pdf: Path, output: Path) -> None:
    reader = PdfReader(pdf)
    writer = PdfWriter()

    for page in reader.pages:
        if "/Contents" in page:
            contents = page["/Contents"]
            if isinstance(contents, IndirectObject):
                contents = contents.get_object()
                
            if isinstance(contents, list):
                for content_obj in contents:
                    if isinstance(content_obj, IndirectObject):
                        content_stream = content_obj.get_object()
                        decompress_content_stream(content_stream)
            elif isinstance(contents, StreamObject): # type: ignore[unreachable]
                decompress_content_stream(contents)


        writer.add_page(page)

    with open(output, "wb") as fp:
        writer.write(fp)

    orig_size = pdf.stat().st_size
    uncomp_size = output.stat().st_size
    ratio = uncomp_size / orig_size
    print(f"Original Size  : {orig_size:,}")
    print(f"Uncompressed Size: {uncomp_size:,} ({ratio * 100:.1f}% of original)")


def decompress_content_stream(content: StreamObject) -> None:  # type: ignore[type-arg]
    if content.get("/Filter") == "/FlateDecode":
        try:
            compressed_data = content.get_data()
            uncompressed_data = zlib.decompress(compressed_data)
            content.set_data(uncompressed_data)
            content.update({"/Filter": None}) # type: ignore[arg-type]
        except zlib.error as e:
            print(f"Decompression error: {e}")
