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
occurences = _occurences,
frequency = _frequency;

- (id) initWithValue: (NSString *)value
       andOccurences: (int)occurences
        andFrequency: (NSNumber *)frequency
{
    self = [super init];
    if (self) {
        _value = value;
        _occurences = occurences;
        _frequency = frequency;
    }
    return self;
}

@end
