from importlib import metadata

print(metadata.version('pip'))
metadata_pip = metadata.metadata("pip")
print(list(metadata_pip))

print(len(metadata.files('pip')))
print(metadata.requires('pip'))