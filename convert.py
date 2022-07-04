import xml.etree.ElementTree as Xet
import pandas as pd
import datetime
import os
import os.path
import sys

def convert():

  time_start = datetime.datetime.now().replace(microsecond=0)
  
  Info_lastNm = []
  Info_firstNm = []
  Info_midNm = []
  Info_indvlPK = []
  Info_actvAGReg = []
  Info_link = []
  OthrNm_lastNm = []
  OthrNm_firstNm = []
  CrntEmp_orgNm = []
  CrntEmp_orgPK = []
  CrntEmp_str1 = []
  CrntEmp_city = []
  CrntEmp_state = []
  CrntEmp_cntry = []
  CrntEmp_postlCd = []
  CrntRgstn_regAuth = []
  CrntRgstn_regCat = []
  CrntRgstn_st = []
  CrntRgstn_stDt = []
  BrnchOfLoc_str1 = []
  BrnchOfLoc_city = []
  BrnchOfLoc_state = []
  BrnchOfLoc_cntry = []
  BrnchOfLoc_postlCd = []

  # CrntRgstn variables
  regAuth_all = ''
  regCat_all = ''
  st_all = ''
  stDt_all = ''

  # BrnchOfLoc variables
  str1_all = ''
  city_all = ''
  state_all = ''
  cntry_all = ''
  postlCd_all = ''

  tree=Xet.parse( 'sample.xml' )
  root=tree.getroot()
  Indvls = list(root[0])
  Indvl = list(Indvls)

  for Indvl_child in Indvl:
    
    # Loop for Info Tag
    for idx, child in enumerate(Indvl_child):
      
      keys = child.attrib.keys()
      
      if len(keys) != 0:
        for k in keys:
          if k == 'lastNm':
            Info_lastNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'firstNm':
            Info_firstNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'midNm':
            Info_midNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'indvlPK':
            Info_indvlPK.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'actvAGReg':
            Info_actvAGReg.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'link':
            Info_link.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

    # Loop for OthrNms Tag
    OthrNms_child = list(Indvl_child[1])

    for child in OthrNms_child:
      
      keys = child.attrib.keys()
      
      if len(keys) != 0:
        for k in keys:

          if k == 'lastNm':
            OthrNm_lastNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'firstNm':
            OthrNm_firstNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

    # Loop for CrntEmps Tag
    CrntEmps_child = list(Indvl_child[2])

    for child in CrntEmps_child:
      
      keys = child.attrib.keys()
      
      if len(keys) != 0:
        for k in keys:

          if k == 'orgNm':
            CrntEmp_orgNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'orgPK':
            CrntEmp_orgPK.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'str1':
            CrntEmp_str1.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'city':
            CrntEmp_city.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'state':
            CrntEmp_state.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'cntry':
            CrntEmp_cntry.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'postlCd':
            CrntEmp_postlCd.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

      # Loop for CrntEmp child nodes
      CrntEmp = list(child)

      for CrntEmp_child in CrntEmp:

        CrntEmp_child_nodes = list(CrntEmp_child)

        for nodes in CrntEmp_child_nodes:

          keys = nodes.attrib.keys()

          print(f'keys - {keys}')
       
          if len(keys) != 0:
            for k in keys:
              if k == 'regAuth':
                regAuth_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

              elif k == 'regCat':
                regCat_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

              elif k == 'st':
                st_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

              elif k == 'stDt':
                stDt_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

              elif k == 'str1':
                str1_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

              elif k == 'city':
                city_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

              elif k == 'state':
                state_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

              elif k == 'cntry':
                cntry_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

              elif k == 'postlCd':
                postlCd_all += nodes.attrib[k] + ','
                print(f'{k}: {nodes.attrib[k]}\n')

      CrntRgstn_regAuth.append(regAuth_all)
      CrntRgstn_regCat.append(regCat_all)
      CrntRgstn_st.append(st_all)
      CrntRgstn_stDt.append(stDt_all)

      BrnchOfLoc_str1.append(str1_all)
      BrnchOfLoc_city.append(city_all)
      BrnchOfLoc_state.append(state_all)
      BrnchOfLoc_cntry.append(cntry_all)
      BrnchOfLoc_postlCd.append(postlCd_all)

  time_end = datetime.datetime.now().replace(microsecond=0)
  runtime = time_end - time_start
  print(f"Script runtime: {runtime}.")

  # Save scraped URLs to a CSV file
  now = datetime.datetime.now().strftime('%Y%m%d-%Hh%M')
  print('Saving to a CSV file...')

  data = {'lastNm': Info_lastNm, 'firstNm': Info_firstNm, 'midNm': Info_midNm, 'indvlPK': Info_indvlPK, 'actvAGReg': Info_actvAGReg, 'link': Info_link, 'OthrNm lastNm': OthrNm_lastNm, 'OthrNm firstNm': OthrNm_firstNm, 'CrntEmp orgNm': CrntEmp_orgNm, 'CrntEmp orgPK': CrntEmp_orgPK, 'CrntEmp str1': CrntEmp_str1, 'CrntEmp city': CrntEmp_city, 'CrntEmp state': CrntEmp_state, 'CrntEmp cntry': CrntEmp_cntry, 'CrntEmp postlCd': CrntEmp_postlCd, 'CrntRgstn regAuth': CrntRgstn_regAuth, 'CrntRgstn regCat': CrntRgstn_regCat, 'CrntRgstn st': CrntRgstn_st, 'CrntRgstn stDt': CrntRgstn_stDt, 'BrnchOfLoc str1': BrnchOfLoc_str1, 'BrnchOfLoc city': BrnchOfLoc_city, 'BrnchOfLoc state': BrnchOfLoc_state, 'BrnchOfLoc cntry': BrnchOfLoc_cntry, 'BrnchOfLoc postlCd': BrnchOfLoc_postlCd}

  df=pd.DataFrame(data=data)
  df.index+=1
  directory = os.path.dirname(os.path.realpath(__file__))
  filename = "convertedXML" + now + ".csv"
  file_path = os.path.join(directory,'csvfiles/', filename)
  df.to_csv(file_path)

  print('Your files are ready.')

if __name__ == '__main__':
    convert()