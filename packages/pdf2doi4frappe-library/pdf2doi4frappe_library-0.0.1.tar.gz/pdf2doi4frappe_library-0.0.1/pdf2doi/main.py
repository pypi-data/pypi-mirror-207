import logging
from os import path, listdir
import pdf2doi.finders as finders
import pdf2doi.config as config
import io


# import easygui Modules that are commented here are imported later only when needed, to improve start up time
# import pyperclip

def pdf2doi(target):
    ''' This is the main routine of the library. When the library is used as a command-line tool (via the entry-point "pdf2doi") the input arguments
    are collected, validated and sent to this function (see the function main() below).
    The function tries to extract the DOI (or other identifiers) of the publication in the pdf files whose path is specified in the input variable target.
    If target contains the valid path of a folder, the function tries to extract the DOI/identifer of all pdf files in the folder.
    It returns a dictionary (or a list of dictionaries) containing info(s) about the file(s) examined, or None if an error occurred.

    Example:
        import pdf2doi
        path = r"Path\to\folder"
        result = pdf2doi.pdf2doi(path)
        print(result[0]['identifier'])          # Print doi/identifier of the first pdf file found in this folder
        print(result[0]['identifier_type'])     # Print the type of identifier found (e.g. 'doi' or 'arxiv')
        print(result[0]['method'])              # Print the method used to find the identifier

    Parameters
    ----------
    target : string
        Relative or absolute path of a .pdf file or a directory containing pdf files

    Returns
    -------
    results, dictionary or list of dictionaries (or None if an error occured)
        The output is a single dictionary if target is a file, or a list of dictionaries if target is a directory,
        each element of the list describing one file. Each dictionary has the following keys

        result['identifier'] = DOI or other identifier (or None if nothing is found)
        result['identifier_type'] = string specifying the type of identifier (e.g. 'doi' or 'arxiv')
        result['validation_info'] = Additional info on the paper. If config.get('webvalidation') = True, then result['validation_info']
                                    will typically contain raw bibtex data for this paper. Otherwise it will just contain True
        result['path'] = path of the pdf file
        result['method'] = method used to find the identifier

    '''

    logger = logging.getLogger("pdf2doi")

    # Check if path is valid
    if not (path.exists(target)):
        logger.error(f"{target} is not a valid path to a file or a directory.")
        return None

    # If target is not a directory, we check that it is an existing file and that it ends with .pdf
    filename = target
    logger.info(f"Trying to retrieve a DOI/identifier for the file: {filename}")
    if not path.exists(filename):
        logger.error(f"'{filename}' is not a valid file.")
        return None
    if not (filename.lower()).endswith('.pdf'):
        logger.error("The file must have .pdf extension.")
        return None
    result = pdf2doi_singlefile(filename)
    if result['identifier'] == None:
        logger.error("It was not possible to find a valid identifier for this file.")

    return result  # This will be a dictionary with all entries as None


def pdf2doi_singlefile(file):
    """
    Try to find an identifier of the file specified by the input argument file.  This function does not check wheter filename is a valid path to a pdf file.

    Parameters
    ----------
    file : ether a string or an object file
                if it's a string, it is the absolute path of a single .pdf file

    Returns
    -------
    result, dictionary
        The output is a single dictionary with the following keys

        result['identifier'] = DOI or other identifier (or None if nothing is found)
        result['identifier_type'] = string specifying the type of identifier (e.g. 'doi' or 'arxiv')
        result['validation_info'] = Additional info on the paper. If config.get('webvalidation') = True, then result['validation_info']
                                    will typically contain raw bibtex data for this paper. Otherwise it will just contain True
        result['path'] = path of the pdf file
        result['method'] = method used to find the identifier

    """

    logger = logging.getLogger("pdf2doi")

    result = {'identifier': None}

    try:
        with open(file, 'rb') as f:
            result = __find_doi(f)
    except TypeError:
        try:
            result = __find_doi(file)
        except Exception:
            logger.exception("File processing error")
    except Exception:
        logger.exception("File(open) processing error")

    return result


def __find_doi(file: io.IOBase) -> dict:
    logger = logging.getLogger("pdf2doi")

    # Several methods are now applied to find a valid identifier in the .pdf file identified by filename

    # First method: we look into the pdf metadata (in the current implementation this is done
    # via the getDocumentInfo() method of the library PyPdf) and see if any of them is a string which containts a
    # valid identifier inside it. We first look for the elements of the dictionary with keys '/doi' or /pdf2doi_identifier'(if the they exist),
    # and then any other field of the dictionary
    logger.info(f"Method #1: Looking for a valid identifier in the document infos...")
    result = finders.find_identifier(file, method="document_infos", keysToCheckFirst=['/doi', '/pdf2doi_identifier'])
    if result['identifier']:
        return result

    # Second method: We look for a DOI or arxiv ID inside the filename
    logger.info(f"Method #2: Looking for a valid identifier in the file name...")
    result = finders.find_identifier(file, method="filename")
    if result['identifier']:
        return result

    # Third method: We look in the plain text of the pdf and try to find something that matches a valid identifier.
    logger.info(f"Method #3: Looking for a valid identifier in the document text...")
    result = finders.find_identifier(file, method="document_text")
    if result['identifier']:
        return result

    # Fourth method: We look for possible titles of the paper, do a google search with them,
    # open the first results and look for identifiers in the plain text of the searcg results.
    logger.info(f"Method #4: Looking for possible publication titles...")
    result = finders.find_identifier(file, method="title_google")
    if result['identifier']:
        return result

    # Fifth method: We extract the first N characters from the file (where N is set by config.get('N_characters_in_pdf')) and we use it as
    # a query for a google seaerch. We open the first results and look for identifiers in the plain text of the searcg results.
    logger.info(
        f"Method #5: Trying to do a google search with the first {config.get('N_characters_in_pdf')} characters of this pdf file...")
    result = finders.find_identifier(file, method="first_N_characters_google")
    if result['identifier']:
        return result

    #If execution arrived to this point, it means that no identifier was found. We still return the dictionary returned by the last attempt, for further processing
    #In this case result['identifier']=None
    return result 


def main():

    # Setup logging
    config.set('verbose', False)

    if target == "":
        print("Error: the following arguments are required: path. Type \'pdf2doi --h\' for a list of commands.")
        return

    if not (path.exists(target)):
        print(f"Error: {target} is not a valid path to a file or a directory.")
        return None

    if not results:
        return
    if not isinstance(results, list):
        results = [results]
    for result in results:
        if result['identifier']:
            print('{:<15s} {:<40s} {:<10s}\n'.format(result['identifier_type'], result['identifier'], result['path']))
        else:
            print('{:<15s} {:<40s} {:<10s}\n'.format('n.a.', 'n.a.', result['path']))

    return


if __name__ == '__main__':
    main()