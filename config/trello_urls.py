# """
# trello URLS factory
# """
# PFM_DOMAIN_MAP = {
#     'US': 'com',
#     'UK': 'co.uk',
#     'CA': 'ca',
#     'DE': 'de',
#     'IN': 'in'
# }
#
#
# class TrelloURLSFactory:
#     @staticmethod
#     def get_urls(pfm):
#         if pfm == 'US':
#             return USTrelloURLs(pfm)
#         else:
#             return TrelloURLS(pfm)
#
#
# class TrelloURLS:
#     def __init__(self, pfm):
#         self.domain = PFM_DOMAIN_MAP[pfm]
#         self.home_page = 'https://www.trello.{}'.format(self.domain)
#         self.sign_in ='https://www.trello.{0}/login'.format(self.domain,
#                                                             pfm.lower() if pfm != 'US' else 'gb')
#         self.sign_out = 'https://trello.{}/logged-out'.format(self.domain)
#
#
# class USTrelloURLs(TrelloURLS):
#     def __init__(self, pfm):
#         super().__init__(pfm)
#         self.sign_in ='https://www.trello.{0}/login'.format(self.domain, 'gb')
#
#
#
