//
//  FrequencyEntry.h
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Entry : NSObject

- (id) initWithValue: (NSString *)value
       andOccurences: (int)occurences
        andFrequency: (NSNumber *)frequency;

@property (copy) NSString *value;
@property int occurences;
@property NSNumber *frequency;

@end
