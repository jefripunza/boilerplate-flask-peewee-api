import os
import pathlib

from flask_swagger_generator.generators import Generator
from flask_swagger_generator.components import SwaggerVersion
from flask_swagger_generator.utils import SecurityType

swagger_destination_path = os.path.join(
            pathlib.Path(__file__).parent.parent.absolute()
        ) + '/swagger.yaml'

# Create swagger version 3.0 generator
autogen_swagger = Generator.of(SwaggerVersion.VERSION_THREE)
generator = autogen_swagger