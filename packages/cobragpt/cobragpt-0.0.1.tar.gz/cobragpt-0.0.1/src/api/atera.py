import argparse
import json
import asyncio
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from aiohttp import ClientSession

parser = argparse.ArgumentParser()
parser.add_argument(
    'invoice',
    type=int,
    help='enter an invoice # to retrieve and generate a pdf',
    default=None
)
parser.add_argument(
    '-f',
    '--filename',
    type=str,
    help='optional name for generated pdf'
)
ARGS = parser.parse_args()

def coord(x, y, unit=1): # pylint: disable=invalid-name
    x, y = x * unit, y * unit
    return x, y

class AteraAPI:
    def __init__(self, endpoint):
        self.url = f'https://app.atera.com/api/v3/{endpoint}'
        self.headers = {
            'Accept': 'application/json',
            'X-API-KEY': 'cf425940016245e99f3fa763c6814fe1'
        }

    async def _get(self, params=None):
        async with ClientSession() as session:
            async with session.get(self.url, headers=self.headers, params=params) as response:
                return await response.json()

    async def _delete(self, params=None):
        async with ClientSession() as session:
            async with session.delete(self.url, headers=self.headers, params=params) as response:
                return await response.json()

    async def _post(self, data=None):
        async with ClientSession() as session:
            data = json.dumps(data)
            async with session.post(self.url, headers=self.headers, data=data) as response:
                return await response.json()

    async def _put(self, data=None):
        async with ClientSession() as session:
            data = json.dumps(data)
            async with session.put(self.url, headers=self.headers, data=data) as response:
                return await response.json()

    def update_endpoint(self, endpoint):
        self.url += f'/{endpoint}'
        return self

    def set_endpoint(self, endpoint):
        self.url = f'https://app.atera.com/api/v3/{endpoint}'
        return self

class Invoice(AteraAPI):
    def __init__(self):
        super().__init__('billing/invoice')
        self.results = {}

    def retrieve(self, invoice_id=None):
        if not invoice_id:
            invoice_id = ARGS.invoice
        super().update_endpoint(invoice_id)
        response = asyncio.run(self._get())
        self.recieve(response)
        return self

    def recieve(self, response):
        self.results = response
        return self

    def get_filename(self):
        return self.results['pdf']

    def set_filename(self):
        invoice_id = self.results['InvoiceNumber']
        file_name = f'Invoice-{invoice_id}'
        if ARGS.filename:
            file_name = ARGS.filename
        return file_name + '.pdf'

    def to_pdf(self, file_name=None):
        if not file_name:
            file_name = self.set_filename()
        canvas = Canvas(file_name)
        canvas.drawString(*coord(1, 1, inch), json.dumps(self.results))
        canvas.save()
        self.results['pdf'] = file_name
        return self

if __name__ == '__main__':
    invoice = Invoice()
    invoice.retrieve()
    invoice.to_pdf()
    outfile = invoice.get_filename()
    print(f"PDF Created Successfully: {outfile}")
