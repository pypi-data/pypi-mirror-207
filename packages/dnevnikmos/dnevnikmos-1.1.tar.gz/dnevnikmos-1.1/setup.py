import setuptools

# Открытие README.md и присвоение его long_description.
with open("README.md", "r") as fh:
	long_description = fh.read()

# Определение requests как requirements для того, чтобы этот пакет работал. Зависимости проекта.
requirements = ["requests<=2.21.0", "selenium"]

# Функция, которая принимает несколько аргументов. Она присваивает эти значения пакету.
setuptools.setup(
	name="dnevnikmos",
	version="1.1",
	author="Boiko Arseniy",
	author_email="ars254642@gmail.com",
	description="Library for automated work with dnevnik.mos.ru",

	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/CyberBars1k/dnevnikmos/",
	packages=setuptools.find_packages(),
	classifiers=[
	],
	python_requires='>=3.6',
)
