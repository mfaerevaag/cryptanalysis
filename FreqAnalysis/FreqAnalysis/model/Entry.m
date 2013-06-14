//
//  FrequencyEntry.m
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import "Entry.h"

@implementation Entry

@synthesize value = _value,
type = _type,
occurences = _occurences,
frequency = _frequency;

- (id) initWithValue: (NSString *)value
       andOccurences: (NSUInteger)occurences
        andFrequency: (NSNumber *)frequency
{
    self = [super init];
    if (self) {
        _value = value;
        _occurences = occurences;
        _frequency = frequency;
        
        switch (value.length) {
            case 1:
                _type = Monogram;
                break;
                
            case 2:
                _type = Bigram;
                break;
                
            case 3:
                _type = Trigram;
                break;
                
            default:
                break;
        }
    }
    return self;
}

+ (NSString *) typeToString: (EntryType)type
{
    switch (type) {
        case Monogram:
            return @"Monogram";
            
        case Bigram:
            return @"Bigram";
            
        case Trigram:
            return @"Trigram";
            
        default:
            break;
    }
}

@end
