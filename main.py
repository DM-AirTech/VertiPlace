from utils import m2ft, ft2m, Pamb, H
from url_builder import url_string_generator
from cli_args import parse_arguments

if __name__ == '__main__':  
    args = parse_arguments() 
    output=url_string_generator(args.api_key, args.lat, args.lon, args.w10, args.w100, args.gust, args.rain, args.t_min, args.t_max, args.p_alt, args.min_fl, args.min_vis, args.min_cbh, args.icing, args.thunder, args.hail, args.blizz, args.hours, args.seasons) 
    output = output.replace("\\","").replace("\"","").replace('n', '') 
    output_list = output.split('_') 
    output_list[1] = float(output_list[1])*100 
    output_list[1] = str(output_list[1]) 
    print('Operability=' + output_list[1] + '%') 
    print('h3_index=' + output_list[0])
