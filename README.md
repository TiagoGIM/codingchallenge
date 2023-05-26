# Quorum Coding Challenge
  Working with Legislative Data.


## Run the application

To run this script and generate the required output files, follow the steps below:

1. Clone this repository to your local machine:
```
$ git clone https://github.com/TiagoGIM/codingchallenge.git
```
2. Navigate to the project directory.
```
$ cd codingchallenge
```
3. Ensure you have Python installed (version 3.6 or higher).
4. Run the script.
```
$  python counting_votes.py
```

The script will process the data and generate the output CSV files.

5. After running the script, the output CSV files will be saved in the project directory:

- legislators-support-oppose-count.csv: Contains the number of bills each legislator supported or opposed.
- bills.csv: Contains information about each bill, including the number of legislators who supported or opposed it and the primary sponsor.

## QUESTIONS AND ANSWERS

### 1. Discuss your solution’s time complexity. What tradeoffs did you make?


- `convert_csv_files_to_dicts_list(files)` [code](https://github.com/TiagoGIM/codingchallenge/blob/0162ec42c59b0558adbf0cca5b0be34c3ad861f4/counting_votes.py#L12) :
   - Time Complexity: O(N*M), where N is the number of files and M is the number of rows in each file.
   - This function iterates over each file and reads its contents using `csv.DictReader`, which has a linear time complexity proportional to the number of rows in the file.

- `map_vote_id_to_bill_id(votes_dic)` [code](https://github.com/TiagoGIM/codingchallenge/blob/0162ec42c59b0558adbf0cca5b0be34c3ad861f4/counting_votes.py#L51):
   - Time Complexity: O(N), where N is the number of rows in the `votes_dic` list.
   - This function iterates over each row in `votes_dic` and maps the `vote_id` to the corresponding `bill_id`. The time complexity is proportional to the number of rows in the list.

Tradeoffs:
- Using `csv.DictReader` to read and convert CSV files into a list of dictionaries is a quick and convenient approach for small to medium-sized datasets. However, it may consume more memory compared to reading the CSV files directly into a DataFrame using libraries like Pandas.
- The tradeoff here is the memory usage versus the ease of use and simplicity of the solution. By loading the data into memory as a list of dictionaries, it allows for easier data manipulation and processing. However, for very large datasets, it might be more memory-efficient to use streaming or incremental processing approaches.

Overall, the time complexity of the solution depends on the size of the input files and the number of rows in each file. The tradeoff made here is favoring simplicity and ease of use over potential memory efficiency for large datasets. I even started with pandas, but since I was asked to code with simplicity and speed, I preferred to validate the use case.

### 2. How would you change your solution to account forfuture columns that might be requested, such as “Bill Voted On Date” or“Co-Sponsors”?

I can edit the method [generate_bills_with_count](https://github.com/TiagoGIM/codingchallenge/blob/0162ec42c59b0558adbf0cca5b0be34c3ad861f4/counting_votes.py#L31) with the `new_prop` and `new_value`.
But it will depend on the business rule.

```
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
            'opposer_count': 0,
            'new_prop': new_value
        }
    return bills
```

### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
The code use of a dictionary structure ,[single_dict](https://github.com/TiagoGIM/codingchallenge/blob/0162ec42c59b0558adbf0cca5b0be34c3ad861f4/counting_votes.py#L105), so updating the 'bills' and 'legislators' keys with the new entries, if the passed list is in a dictionary format, as shown in the example below.


```
single_dict = convert_csv_files_to_dicts_list(file_names)

single_dict['legislators'] = LIST OF LEGISLATORS

single_dict['bills'] = LIST OF BILLS

votes_result = count_votes(single_dict)
```

### 4. How long did you spend working on the assignment?

I spent around 35 to 40 minutes reading the problem and creating the first draft. Then, I spent one hour refactoring and adding the last part of the code to save the files. 
