import os
import multiprocessing as mp
import pandas as pd
import numpy as np
import hashlib
import random

'''
Based on: https://github.com/kumparan/kumparanian/blob/master/kumparanian/de/dataset.py
'''
__CITIES__ = pd.read_csv('cities.csv')
__JOBS__ = pd.read_csv('jobs.csv')


class DataGenerator:
    def __init__(self, name, num_files=5, output_dir='data'):
        self.name = name
        self.num_files = num_files
        self.output_dir = output_dir
        self.__abc = 'abcdefghijklmnopqrstuvwxyz'
        self.__generate_random_properties()

    def encode_st(self, st: str):
        temp = ''
        temp += self.__abc[int(st[0])]
        temp += self.__abc[int(st[1])]
        for i in range(len(st[2:])):
            if i % 2 == 0:
                temp += st[i+2]
            else:
                temp += self.__abc[int(st[i+2])]
        return temp

    def __generate_random_properties(self):
        assert self.name, 'Please assign your name'
        print('[GLCRBM] Initializing ...')
        # Set random seed to get a consistent output
        hex_digest = hashlib.sha1(self.name.encode("utf-8")).hexdigest()
        random_seed_int = int(hex_digest, 16) % (5**12)
        np.random.seed(random_seed_int)
        random.seed(random_seed_int)
        # Generating the number
        self.__MAX_DATA__ = 500  # Generated over 50 MB data

        # Generating id (Used for every file)
        self.__MAX_INT_DATA = 2**40-1
        self.__RANDOM_NUMBER__ = np.random.randint(low=0,
                                                   high=self.__MAX_INT_DATA,
                                                   size=self.__MAX_DATA__,
                                                   dtype=np.int64)
        temp = np.unique(self.__RANDOM_NUMBER__)
        def encoder(x): return self.encode_st(str(x))
        self.__LIST_OF_ACCOUNT_ID__ = [encoder(x) for x in temp]
        gender = ['male', 'female']
        # Account balance is either increase or decrease by the income or spend.
        # Current balance =last month balance+income-spend
        # This initial balance should be reformulated
        self.__BALANCE_LIST__ = np.random.wald(
            mean=15000, scale=10, size=self.__MAX_DATA__).astype(int)*1000
        # For job, we mapping between the ID with the jobs number. It's randomized but should works fine
        self.__ACCOUNT_LIST__ = {acid: {'balance': init_bl, 'job': random.choice(__JOBS__.jobs), 'city': random.choice(
            __CITIES__.Cities), 'gender': random.choice(gender)} for acid, init_bl in zip(self.__LIST_OF_ACCOUNT_ID__, self.__BALANCE_LIST__)}
        self.__BASE_SALARY__ = 3800000
        print('[GLCRBM] Initializing ... Done!')

    
    def generate_data_per_month(self, output_file, number):
        """Generate partition given random seed and output file """
        print("[GLCRBM]: Generating {} ...".format(output_file))

        # Create the output directory if not exist
        output_dir = os.path.dirname(output_file)
        os.makedirs(output_dir, exist_ok=True)

        # Generating the pair of id and number
        num_max_data = min(len(self.__LIST_OF_ACCOUNT_ID__), self.__MAX_DATA__)

        # Month:
        def month(number): return number+1 if number + \
            1 <= 12 else (number % 12)+1  # Month in number

        header = '''account_id,last_month_balance,city,gender,job,month,active_income,passive_income'''
        f = open(output_file, "w")
        f.write(header)
        for i in range(0, num_max_data):
            temp_acc_id = self.__LIST_OF_ACCOUNT_ID__[i]
            # print('account_id', temp_acc_id)
            temp_acc = self.__ACCOUNT_LIST__[temp_acc_id]
            # print('temp acc', temp_acc)
            last_mont_balance = temp_acc['balance']
            activ = __JOBS__[__JOBS__.jobs == temp_acc['job']
                             ].salary_coef.values * self.__BASE_SALARY__
            pasiv = 0
            row = "{acid},{lmbln},{ct},{gnd},{job},{mn},{activ},{pasiv}".format(
                acid=self.__LIST_OF_ACCOUNT_ID__[i],
                lmbln=last_mont_balance,
                ct=temp_acc['city'],
                gnd=temp_acc['gender'],
                job=temp_acc['job'],
                mn=month(number),
                activ=int(activ[0]),
                pasiv=pasiv
            )
            self.__ACCOUNT_LIST__[
                temp_acc_id]['balance'] += int(activ[0])+pasiv
            # self.__BALANCE_LIST__[i] = self.__BALANCE_LIST__[i]+0
            f.write("\n{}".format(row))
        f.close()
        print("[GLCRBM]: Generating {} ... DONE".format(output_file))

    def generate_data_parallel(self):
        """Generate assesment data given output_dir """
        random_seed_template = 'data_glcrbm_{{num:02d}}'
        output_template = '{dir}/data_glcrbm_{{num:02d}}.csv'.format(
            dir=self.output_dir)
        # Generating NUM_FILES files that each have size of 100mb
        # We generate in parallel to speed up
        # We use up to 4 workers in parallel
        # default num_files = 40, approximately around 4.4 GB, separated into 40 files (100MB/file)
        # with 6270700 rows per files. 10 files = ~1 GB
        # To measure the performace of AWS Redshift, num_files should be around
        # 1 TB = 1.000 GB, then this should be alocated into 10.000 files
        # 12 for -> 4 or 2 worker
        print('[GLCRBM]: Generating 1 TB data. Paralel with {nw} workers. Prepare yourself. Get some snack and watch!'.format(
            nw=mp.cpu_count()))
        with mp.Pool(processes=mp.cpu_count()) as pool:
            for i in range(0, self.num_files):
                output_file = output_template.format(num=i)
                pool.apply_async(self.generate_data_per_month,
                                 (output_file, i))
            pool.close()
            pool.join()
        print("[GLCRBM]: Generating {num} data is done. JK, it's not even 1 TB data. Have fun!".format(
            num=self.num_files))

    def generate_data(self):
        """Generate assesment data given output_dir """
        random_seed_template = 'data_glcrbm_{{num:02d}}'
        output_template = '{dir}/data_glcrbm_{{num:02d}}.csv'.format(
            dir=self.output_dir)
        print(
            '[GLCRBM]: Generating 1 TB data. Prepare yourself. Get some snack and watch!')
        for i in range(0, self.num_files):
            output_file = output_template.format(num=i)
            self.generate_data_per_month(output_file, i)
        print("[GLCRBM]: Generating {num} data is done. JK, it's not even 1 TB data. Have fun!".format(
            num=self.num_files))

if __name__ == "__main__":
    nama = 'Harits' # change with your name
    event_generator = DataGenerator(nama)
    event_generator.generate_data()
    
