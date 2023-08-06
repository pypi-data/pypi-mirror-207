import click

from .PDFParserClass import *

obj_parser = PDFparser()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('input_file', type=click.Path(exists=True)) #Compulsory argument for input PDF file
@click.option('--output_file', '-o', type=str,default='pdf_output.txt', help='Name of the output file') #Optional flag to select a specific output file name
def pdftotext(input_file,output_file):
    """
    Convert a PDF file into text file.
    """
    obj_parser.pdftotext(input_file,output_file)


@cli.command()
@click.argument('input_file', type=click.Path(exists=True)) #Compulsory argument for input PDF file
@click.option('--output_file', '-o', type=str,default='pdf_output.json', help='Name of the output file') #Optional flag to select a specific output file name
def pdftojson(input_file,output_file):
    """
    Convert a PDF file into JSON file.
    """
    obj_parser.simplePdftoJson(input_file,output_file)

@cli.command()
@click.argument('input_file', type=click.Path(exists=True)) #Compulsory argument for input PDF file
@click.option('--output_file', '-o', type=str,default='pdf_output.jsonl', help='Name of the output file') #Optional flag to select a specific output file name
def pdftojsonl(input_file,output_file):
    """
    Convert a PDF file into JSONL file.
    """
    obj_parser.pdftojsonl(input_file,output_file)

# Call click.cli() to start the CLI application
if __name__ == '__main__':
    cli()