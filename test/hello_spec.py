from mamba import description, context, it
from expects import expect, equal

with description('Hello Mamba') as self:

    with it('fails this test'):
        expect(2).to(equal(3))

    with it('pass this test'):
        expect(2).to(equal(2))