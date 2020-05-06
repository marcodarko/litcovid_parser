import os

import biothings, config
biothings.config_for_app(config)

import biothings.hub.dataload.uploader

# when code is exported, import becomes relative
try:
    from litcovid_parser.parser import load_annotations as parser_func
except ImportError:
    from .parser import load_annotations as parser_func


class LitCovidUploader(biothings.hub.dataload.uploader.BaseSourceUploader):

    name = "litcovid"
    __metadata__ = {"src_meta": {}}
    idconverter = None
    storage_class = biothings.hub.dataload.storage.BasicStorage

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return parser_func(data_folder)

    @classmethod
    def get_mapping(klass):
        return  {
                    'fields':{
                        'type': 'text'
                    },
                    'abstract': {
                        'type': 'text'
                    },
                    '@type': {
                        'type': 'text'
                    },
                    'pmid': {
                        'type': 'integer'
                    },
                    'author': {
                        # 'type': 'nested',
                        'properties': {
                            'name':{
                                'type': 'text'
                            },
                            'givenName':{
                                'type': 'text'
                            },
                            'familyName':{
                                'type': 'text'
                            },
                            'affiliation':{
                                # 'type': 'nested',
                                'properties': {
                                    'name':{
                                        'type': 'text'
                                    }
                                }
                            }
                        }
                    },
                    'isBasedOn': {
                        'type': 'text'
                    },
                    'funding': {
                        # 'type': 'nested',
                        'properties': {
                            'funder':{
                                # 'type': 'nested',
                                'properties':{
                                    'name': {
                                        'type': 'text'
                                    }
                                }
                            },
                            'identifier':{
                                'type': 'text'
                            }
                        }
                    },
                    'license': {
                        'type': 'text'
                    },
                    'keywords': {
                        'normalizer': 'keyword_lowercase_normalizer',
                        'type': 'keyword',
                        'copy_to': ['all']
                    },
                    'publicationType': {
                        'normalizer': 'keyword_lowercase_normalizer',
                        'type': 'keyword',
                        'copy_to': ['all']
                    },
                    'name': {
                        'type': 'text'
                    },
                    'journalName': {
                        'type': 'text'
                    },
                    'identifier': {
                        'type': 'text'
                    },
                    'doi': {
                        'type': 'text'
                    },
                    'datePublished': {
                        'type': 'keyword'
                    },
                    'dateModified': {
                        'type': 'keyword'
                    },
                    'issueNumber': {
                        'type': 'text'
                    }
                }
