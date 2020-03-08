from mamba import description, context, it, _it
from expects import expect, equal

with description('Hello Mamba') as self:

    with _it('fails this test'):
        expect(2).to(equal(3))

    with _it('pass this test'):
        expect(2).to(equal(2))