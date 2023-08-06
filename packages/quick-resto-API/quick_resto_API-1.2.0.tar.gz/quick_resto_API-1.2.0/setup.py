from distutils.core import setup
from pathlib import Path

setup(
    name="quick_resto_API",
    version="1.2.0",
    description='Quick Resto API',
    packages=['quick_resto_API', 'quick_resto_API.operations_with_objects.modules', 'quick_resto_API.operations_with_objects', 
                'quick_resto_API.quick_resto_objects.modules.alcohol', 'quick_resto_API.quick_resto_objects.modules.core',
                'quick_resto_API.quick_resto_objects.modules.crm','quick_resto_API.quick_resto_objects.modules.front',
                'quick_resto_API.quick_resto_objects.modules.personnel','quick_resto_API.quick_resto_objects.modules.warehouse',
                'quick_resto_API.quick_resto_objects.platform','quick_resto_API.quick_resto_objects'],

    author_email='sergey.rukin1425@gmail.com',
    author='sergeyrukin',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
)