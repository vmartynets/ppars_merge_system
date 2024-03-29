from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from ppars.apps.charge.models import Charge
from ppars.apps.core.models import CompanyProfile


class Command(BaseCommand):
    '''
    dec_usaepay
    '''

    def handle(self, *args, **options):
        print "start"
        ref_nums = ['837928068', '837928092', '837928104', '837928112',
                    '837928162', '838207983', '838598598', '839052898',
                    '839053493', '839455268', '839455490', '839457144',
                    '840300564', '840621944', '840622013', '840622261',
                    '840622288', '841372289', '842889098', '843325657',
                    '843325717', '843567182', '843922485', '844335200',
                    '844335224', '844335253', '845029557', '845029559',
                    '845029572', '845029588', '845029601', '845029607',
                    '845344286', '845567106', '845691536', '845691545',
                    '845732108', '845732199', '845732216', '846058828',
                    '846059940', '846060095', '846481955', '846481968',
                    '846482011', '847572014', '847572017', '847572026',
                    '848277954', '849970689', '850768074', '850768102',
                    '850768146', '851202442', '851516954', '851516996',
                    '851517024', '851517038', '851517040', '851518023',
                    '851518825', '852943063', '852943134', '853306887',
                    '853710058', '854071638', '854071683', '856140319',
                    '856290306', '856489554', '856489962', '856993673',
                    '856993678', '856993685', '857218751', '857219014',
                    '857219186', '857219313', '857219604', '857219619',
                    '857668601', '857669249', '857669483', '857967518',
                    '857967626', '857967628', '857967731', '858980373',
                    '859137650', '859313152', '859313383', '859313481',
                    '859314581', '859315424', '859685786', '859685790',
                    '859726567', '859726599', '859726693', '859726692',
                    '859726719'
]
        for company in CompanyProfile.objects.filter(superuser_profile=False):
            print company
            for charge in Charge.objects.filter(company=company, payment_getaway=Charge.USAEPAY):
                if charge.atransaction in ref_nums:
                    print '%s%s' % (settings.SITE_DOMAIN, reverse('charge_detail', args=[charge.id]))
        print "done"