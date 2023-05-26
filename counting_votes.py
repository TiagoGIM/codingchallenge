import csv


def process_data():
    legislators = {}
    bills = {}
    voted_bill = {}
    vote_results = {}

# Reading files and populating dicts.
    with open('legislators.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            legislator_id = int(row['id'])
            legislator_name = row['name']
            legislators[legislator_id] = {
                'id': legislator_id,
                'name': legislator_name,
                'num_supported_bills': 0,
                'num_opposed_bills': 0

            }

    with open('bills.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            bill_id = int(row['id'])
            bill_title = row['title']
            primary_id = int(row['sponsor_id'])
            primary_sponsor = 'Unknown'
            if primary_id in legislators:
                primary_sponsor = legislators[legislator_id]['name']

            bills[bill_id] = {
                'id': int(row['id']),
                'title': bill_title,
                'primary_sponsor': primary_sponsor,
                'supporter_count': 0,
                'opposer_count': 0
            }

    with open('votes.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vote_id = int(row['id'])
            bill_id = int(row['bill_id'])
            voted_bill[vote_id] = bill_id

# Calculating votes
    with open('vote_results.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vote_result_id = int(row['id'])
            legislator_id = int(row['legislator_id'])
            vote_id = int(row['vote_id'])
            vote_type = int(row['vote_type'])
            vote_results[vote_result_id] = {
                'legislator_id': legislator_id,
                'bill_id': voted_bill[vote_id],
                'vote_type': vote_type
            }
            if vote_type == 1:
                bills[voted_bill[vote_id]]['supporter_count'] = bills[voted_bill[vote_id]
                                                                      ]['supporter_count'] + 1
                legislators[legislator_id]['num_supported_bills'] = legislators[legislator_id]['num_supported_bills'] + 1
            elif vote_type == 2:
                legislators[legislator_id]['num_opposed_bills'] = legislators[legislator_id]['num_opposed_bills'] + 1
                bills[voted_bill[vote_id]]['opposer_count'] = bills[voted_bill[vote_id]
                                                                    ]['opposer_count'] + 1
    print(legislators, bills)


# Run the data processing
process_data()


# Generate output CSV files legislators-support-oppose-count.csv and bills.csv
