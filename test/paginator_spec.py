from mamba import description, context, it, _it
from expects import expect, equal

from simplertimes.lib.paginator import *

with description('Paginator') as self:

    with it('instantiates the class'):
        p = Paginator()
        expect(p.__class__.__name__).to(equal('Paginator'))
