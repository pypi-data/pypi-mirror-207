import os, shutil
import logging
from pdf2image import convert_from_path

from mkdocs.config import base, config_options as c
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File

# class _Annexe(base.Config):
#     src = c.File(exists=True)
#     dest = c.Type(str, default=src)
#     num = c.Optional(c.Type(int))

class AnnexesIntegrationConfig(base.Config):
    temp_dir = c.Type(str, default='temp_annexes')
    annexes = c.ListOfItems(c.Type(dict)) # c.SubConfig(_Annexe)

class AnnexesIntegration(BasePlugin[AnnexesIntegrationConfig]):

    def __init__(self):
        self._logger = logging.getLogger('mkdocs.annexes-integration')
        self._logger.setLevel(logging.INFO)

        self.enabled = True
        self.total_time = 0
    
    def on_config(self, config):
        self.config.temp_dir = os.path.join(os.path.dirname(config.docs_dir), self.config.temp_dir)
        if not os.path.exists(self.config.temp_dir):
            os.mkdir(self.config.temp_dir)
        return config

    def on_files(self, files, config):
        try:
            for annex in self.config.annexes:
                title, path = list(annex.items())[0]
                self._logger.info(f'Integrating annex "{title}"')
                src, dest = self.get_src_and_dest(path)
                extension = os.path.splitext(src)[1][1:]
                original = os.path.join(config.docs_dir, src)
                root = os.path.join(self.config.temp_dir, os.path.splitext(dest)[0])
                embedded = f'{root}.md'
                if os.path.exists(original):
                    if extension in ['cs', 'css', 'dart', 'html', 'js', 'json', 'php']:
                        self._logger.info(f'    With content as code block')
                        with open(original, 'r') as file:
                            content = file.read()
                        # Create a markdown file that take care of showing source code annex
                        if not os.path.exists(os.path.dirname(embedded)):
                            os.makedirs(os.path.dirname(embedded))
                        with open(embedded, 'w') as f:
                            # write the title and the content to the file
                            f.write(f'# {title}\n\n``` {extension}\n{content}\n```\n')
                    elif extension in ['pdf']:
                        self._logger.info(f'    With each pages as images')
                        source = os.path.join(root, 'source')
                        # Create a root folder containing the annex
                        if not os.path.exists(root):
                            os.makedirs(root)
                        # Save pages as images in the pdf
                        images = convert_from_path(original)
                        # Create source folder to save images
                        if not os.path.exists(source):
                            os.mkdir(source)
                        # Create a markdown file that take care of showing PDF annex
                        with open(embedded, 'w') as f:
                            # write the title to the file
                            f.write(f'# {title}\n\n')

                            for i in range(len(images)):
                                # Add leading zeros to the page number
                                filename = f'page_{i + 1:04}.jpg'
                                images[i].save(f'{source}/{filename}', 'JPEG')
                                files.append(File(os.path.join(os.path.splitext(dest)[0], f'source/{filename}'), src_dir=self.config.temp_dir, dest_dir=config.site_dir, use_directory_urls=config.use_directory_urls))

                                # write the image link to the file
                                f.write(f'![Page {i+1}](./{os.path.basename(os.path.splitext(dest)[0])}/source/{filename})\n')
                    else:
                        self._logger.warning(f'file {src} extension isn\'t supported (yet) --> skipped')
                    # removing originals files from list of mkdocs files if they were in the docs directory originaly
                    if os.path.isfile(os.path.join(config.docs_dir, dest)):
                        self._logger.info(f'    Remvoing original annex {src} from processed files list')
                        files.remove(files.get_file_from_path(src))
                    # adding embedded files in list of mkdocs files
                    path = f'{os.path.splitext(dest)[0]}.md'
                    self._logger.info(f'    Adding embedded annex {dest} to processed files list')
                    files.append(File(path, src_dir=self.config.temp_dir, dest_dir=config.site_dir, use_directory_urls=config.use_directory_urls))
                else:
                    self._logger.warning(f'{src} file doesn\'t exist at {original} --> skipped')
        except Exception as e:
            self._logger.error(f'error with the annexes-integration plugin : {e}')
            if os.path.exists(self.config.temp_dir):
                shutil.rmtree(self.config.temp_dir)
            raise e
        return files
    
    def on_post_build(self, config):
        # Removing temp_dir directory
        self._logger.info(f'Removin annexes temporary directory {self.config.temp_dir}')
        if os.path.exists(self.config.temp_dir):
            shutil.rmtree(self.config.temp_dir)
        return
    
    def get_src_and_dest(self, path):
        if type(path) is dict:
            src = path['src']
            dest = src
            while (dest.startswith('../')):
                dest = dest[3:]
            if 'dest' in path:
                dest = path['dest']
        else:
            src = path
            dest = src
            while (dest.startswith('../')):
                dest = dest[3:]
        if os.path.splitext(os.path.basename(dest))[0] == 'index':
            dest = os.path.join(os.path.dirname(dest), f'_{os.path.basename(dest)}')
        return src, dest
    
    def get_file_ext(self, src):
        return os.path.splitext(src)[1][1:]
    
    def get_orig_path(self, docs_dir, src):
        return os.path.join(docs_dir, src)
    
    def get_temp_path(self):
        return
    
    def get_dest_path(self):
        return
    
    def get_filename(dest):
        return
