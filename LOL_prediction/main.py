# -*- coding: utf-8 -*-
import requests
from urllib import parse
import json
import pickle

def apiKey():
    return DEVELOPMENTAPIKEY

def encryptaccountId(data):
    return data["accountId"]

def match_data(matchId):
    match_APIURL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + str(matchId)
    match_res = requests.get(match_APIURL, headers=headers)
    match_data = match_res.json()
    return match_data

def bring_5_games(id,matchId):
    each_matchlist_APIURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + id
    each_matchlist_res = requests.get(each_matchlist_APIURL, headers=headers)
    each_matchlist_data = each_matchlist_res.json()
    count = 0

    for i in each_matchlist_data["matches"]:
        if i["gameId"] == matchId:
            break
        else:
            count += 1
    temp_list = list()
    for i in range(count + 1, count + 6):
        temp_list.append(each_matchlist_data["matches"][i]["gameId"])

    each_summoner_matches[id] = (temp_list)

    return each_summoner_matches

if __name__ == "__main__":

    summonerName = "Hide on bush"
    DEVELOPMENTAPIKEY = "RGAPI-6cb52e6e-fc5c-4adc-b5fb-8ae92d4fd3f7"
    encodingSummonerName = parse.quote(summonerName)

    ######## 소환사의 암호화 된 ID받아오기 ###########

    summoner_APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
    summoner_res = requests.get(summoner_APIURL, headers=headers)
    summoner_data = summoner_res.json()

    print(summoner_data)
    encryptId = encryptaccountId(summoner_data)



    ######## 암호화된 Id를 통해 소환사의 최근 matchlist를 불러온다 ########


    matchlist_APIURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptId
    matchlist_res = requests.get(matchlist_APIURL, headers=headers)
    matchlist_data = matchlist_res.json()


    ####### 0번 인덱스의 match 정보 불러오기 ################



    summonerName = summonerName.replace(" ", "").lower() #소환사 이름이 필요한가....?


    matchId = matchlist_data['matches'][0]['gameId']

    match_data = match_data(matchId)
    print(match_data)

    jsonform = json.dumps(match_data['participantIdentities'],indent=4) #해당 게임에 참여한 사람들의 정보

    # print(jsonform)


    ######### match의 소환사들의 해당 게임 직전 5게임 Id 받아오기 ############


    summoner_id_list = list()

    for j in match_data["participantIdentities"]:
        summoner_id_list.append(j['player']['accountId'])


    each_summoner_matches = dict()

    for id in summoner_id_list:
        each_matchlist_APIURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + id
        each_matchlist_res = requests.get(each_matchlist_APIURL, headers=headers)
        each_matchlist_data = each_matchlist_res.json()
        count = 0

        for i in each_matchlist_data["matches"]:
            if i["gameId"] == matchId:
                break
            else :
                count+=1
        temp_list = list()
        for i in range(count+1,count+6):
            temp_list.append(each_matchlist_data["matches"][i]["gameId"])

        each_summoner_matches[id] = (temp_list)
    print(each_summoner_matches)

    for key in each_summoner_matches:
        for match in each_summoner_matches[key]:

            match_APIURL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + str(match)
            match_res = requests.get(match_APIURL, headers=headers)
            match_data = match_res.json()

            for i in range(0,10):
                if match_data["participantIdentities"][i]["player"]["accountId"] == key:
                    print(type(match_data["participants"][i]))














