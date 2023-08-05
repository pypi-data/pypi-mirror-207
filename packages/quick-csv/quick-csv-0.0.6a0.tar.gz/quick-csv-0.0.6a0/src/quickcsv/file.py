import csv
from collections import OrderedDict

def read_csv(csv_path,fields=None,func_row=None,func_row_field=None,encoding='utf-8'):
    '''
        read csv file as a list of model dictionaries
    '''
    return qc_read(csv_path=csv_path,fields=fields,func_row=func_row,func_row_field=func_row_field,encoding=encoding)

def write_csv(save_path,list_rows=None,encoding='utf-8'):
    '''
        write csv file with a list of model dictionaries
    '''
    return qc_write(save_path=save_path,list_rows=list_rows,encoding=encoding)

def read_csv_gbk(csv_path,fields=None,func_row=None,func_row_field=None):
    '''
        read csv file as a list of model dictionaries in GBK encoding
    '''
    return qc_read(csv_path=csv_path,fields=fields,func_row=func_row,func_row_field=func_row_field,encoding='gbk')

def write_csv_gbk(save_path,list_rows=None):
    '''
        write csv file with a list of model dictionaries in GBK encoding
    '''
    return qc_write(save_path=save_path,list_rows=list_rows,encoding='gbk')

def write_text(file_path,str,encoding='utf-8',mode='w'):
    '''
        write plain text content
    '''
    return qc_twrite(file_path=file_path,str=str,encoding=encoding,mode=mode)

def read_text(file_path,encoding='utf-8',mode='r'):
    '''
        read plain text content
    '''
    return qc_tread(file_path=file_path,encoding=encoding,mode=mode)

def qc_read(csv_path,fields=None,func_row=None,func_row_field=None,encoding='utf-8'):
    if fields==None:
        return quick_read_csv_model(csv_path,func_row=func_row,encoding=encoding)
    else:
        return quick_read_csv(csv_path,fields,func_row=func_row,func_row_field=func_row_field,encoding=encoding)

def qc_write(save_path,list_rows=None,encoding='utf-8'):
    return quick_save_csv(save_path=save_path,list_rows=list_rows,encoding=encoding)

def qc_twrite(file_path,str,encoding='utf-8',mode='w'):
    f_out=open(file_path,mode,encoding=encoding)
    f_out.write(str)
    f_out.close()

def qc_tread(file_path,encoding='utf-8',mode='r'):
    f_in=open(file_path,mode,encoding=encoding)
    result=f_in.read()
    return result

def quick_read_csv(csv_path,fields,func_row=None,func_row_field=None,encoding='utf-8'):
    with open(csv_path, newline='',encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        list_result=[]
        for row in reader:
            l=[]
            if func_row!=None:
                func_row(row)
            for f in fields:
                if func_row_field!=None:
                    func_row_field(f,row[f])
                l.append(row[f])
            list_result.append(l)
        return list_result

def quick_read_csv_model(csv_path,encoding='utf-8',func_row=None):
    list_result=[]
    keys=[]
    with open(csv_path, newline='',encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keys=list(row.keys())
            if func_row!=None:
                func_row(row)
            list_result.append(row)
    print(f"Read CSV:",keys,f" <- ({csv_path})")
    return list_result

def quick_save_csv(save_path,field_names=None,list_rows=None,encoding='utf-8',mode='w'):
    if field_names==None:
        field_names=[]
        if len(list_rows)==0:
            raise Exception("To infer the field names of data during saving, please ensure the list is NOT empty!")
        model=list_rows[0]
        for k in model.keys():
            field_names.append(k)
    with open(save_path, mode, newline='',encoding=encoding) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        if list_rows!=None:
            for row in list_rows:
                dict_model = {}
                for f in field_names:
                    dict_model[f]=row[f]
                writer.writerow(dict_model)
    print("Write CSV:", field_names , f" -> ({save_path})")

def quick_remove_unicode(str,encoding='gbk',decoding='gbk'):
    string_encode = str.encode(encoding, "ignore")
    string_decode = string_encode.decode(decoding)
    return string_decode

def quick_align_list_model(list_item):
    '''
        ensure all models in the list have a same key set, call it before save csv
    '''
    all_keys=[]
    for item in list_item:
        for k in item:
            if k not in all_keys:
                all_keys.append(k)
    for idx,item in enumerate(list_item):
        for k in all_keys:
            if k not in item:
                list_item[idx][k]=""
    return list_item

def create_df(list_item):
    import pandas as pd
    dict_values={}
    for item in list_item:
        for k in item:
            if k in dict_values:
                dict_values[k].append(item[k])
            else:
                dict_values[k]=[item[k]]
    df = pd.DataFrame(data=dict_values)
    return df

def to_sorted_dict(dict,reverse=True):
    '''
    Convert a dict to ordered dict
    '''
    dict = OrderedDict(sorted(dict.items(), key=lambda obj: obj[1], reverse=reverse))
    return dict

def quick_combine_csv(csv_path1,csv_path2,use_field=None,save_csv_path=None,remove_duplicate=True):
    '''
    Combine two csv files into a single CSV file according to settings.
    '''
    list_item1 = read_csv(csv_path1)
    list_item2 = read_csv(csv_path2)

    if use_field==None:
        use_field=list(list_item1[0].keys())[0]

    print(f"Combining two csv files according to [{use_field}]")

    list_all = []
    list_id = []
    for item in list_item1:
        url = item[use_field]
        if remove_duplicate:
            if url in list_id:
                continue
        list_all.append(item)
        list_id.append(url)

    for item in list_item2:
        url = item[use_field]
        if remove_duplicate:
            if url in list_id:
                continue
        list_all.append(item)
        list_id.append(url)
    if save_csv_path!=None:
        write_csv(save_csv_path, list_all)
    return list_all
