import csv


file_names = ["bills", "legislators", "vote_results", "votes"]


def convert_csv_files_to_dicts_list(files):
    data = {}
    for file in files:
        with open(file+'.csv', 'r') as f:
            data[file] = list(csv.DictReader(f))
    return data


def generate_legislator_with_count(dict_legislators):
    legislators = {}
    for legislator in dict_legislators:

        legislator_id = int(legislator['id'])
        legislators[legislator_id] = {
            'id': legislator_id,
            'name': legislator['name'],
            'num_supported_bills': 0,
            'num_opposed_bills': 0,

        }

    return legislators


def generate_bills_with_count(legislators_mapped, dic_bills):
    bills = {}
    for bil in dic_bills:
        bill_id = int(bil['id'])
        bill_title = bil['title']
        primary_id = int(bil['sponsor_id'])
        primary_sponsor = 'Unknown'
        if primary_id in legislators_mapped:
            primary_sponsor = legislators_mapped[primary_id]['name']
        bills[bill_id] = {
            'id': int(bil['id']),
            'title': bill_title,
            'primary_sponsor': primary_sponsor,
            'supporter_count': 0,
            'opposer_count': 0
        }
    return bills


def map_vote_id_to_bill_id(votes_dic):
    bills_id = {}
    for row in votes_dic:
        vote_id = int(row['id'])
        bill_id = int(row['bill_id'])
        bills_id[vote_id] = bill_id
    return bills_id


def count_votes(dict_files):

    legislators = generate_legislator_with_count(
        dict_files['legislators'])

    bills = generate_bills_with_count(
        legislators, dict_files['bills'])

    mapped_bill_vote = map_vote_id_to_bill_id(dict_files['votes'])

    for vote in dict_files['vote_results']:
        legislator_id = int(vote['legislator_id'])
        vote_id = int(vote['vote_id'])
        vote_type = int(vote['vote_type'])

        bill_id = mapped_bill_vote[vote_id]

        if vote_type == 1:
            bills[bill_id]['supporter_count'] = bills[bill_id]['supporter_count'] + 1
            legislators[legislator_id]['num_supported_bills'] = legislators[legislator_id]['num_supported_bills'] + 1
        elif vote_type == 2:
            legislators[legislator_id]['num_opposed_bills'] = legislators[legislator_id]['num_opposed_bills'] + 1
            bills[bill_id]['opposer_count'] = bills[bill_id]['opposer_count'] + 1

    return {'legislators': legislators, 'bills': bills}


single_dict = convert_csv_files_to_dicts_list(file_names)

votes_result = count_votes(single_dict)
# Generate output CSV files legislators-support-oppose-count.csv and bills.csv
