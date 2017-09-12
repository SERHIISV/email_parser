import os


filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mbox.txt')

edata = dict()


def parse(filepath):
    with open(filepath) as f:
        content = f.read()

    emails = content.split('\n\n\n')
    for eml in emails:
        for el in eml.split('\n'):
            if el.startswith('Author:'):
                email = el.strip('Author: ')
            elif el.startswith('Date:'):
                date = el.strip('Date: ')
            elif el.startswith('Subject:'):
                subject = el.strip('Subject: ')

        if not edata.get(email):
            edata[email] = 1
        else:
            edata[email] += 1

        print '{} ({}): {}'.format(email, date, subject)

    for el in edata:
        print '{}: {}'.format(el, edata[el])

if __name__ == "__main__":
    parse(filepath)
