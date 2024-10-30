"""
Module for uncompressing PDF content streams.
"""

from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import IndirectObject
import zlib


def main(pdf: Path, output: Path) -> None:
    reader = PdfReader(pdf)
    writer = PdfWriter()

    for page in reader.pages:
        if "/Contents" in page:
            contents = page["/Contents"]
            if isinstance(contents, IndirectObject):
                contents = contents.get_object()
            # Handle multiple content streams or single
            if isinstance(contents, list):
                for content in contents:
                    decompress_content_stream(content)
            else:
                decompress_content_stream(contents)
        writer.add_page(page)

    with open(output, "wb") as fp:
        writer.write(fp)

    orig_size = pdf.stat().st_size
    uncomp_size = output.stat().st_size

    print(f"Original Size  : {orig_size:,}")
    print(f"Uncompressed Size: {uncomp_size:,} ({(uncomp_size / orig_size) * 100:.1f}% of original)")


def decompress_content_stream(content: IndirectObject) -> None:
    """Decompress a content stream if it uses FlateDecode"""
    if content.get("/Filter") == "/FlateDecode":
        try:
            compressed_data = content.get_data()
            uncompressed_data = zlib.decompress(compressed_data)
            content.set_data(uncompressed_data)
            del content["/Filter"]  # Remove compression flag
        except zlib.error as e:
            print(f"Decompression error: {e}")
