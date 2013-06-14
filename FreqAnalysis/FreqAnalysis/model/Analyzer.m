//
//  Analyzer.m
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import "Analyzer.h"
#import "Entry.h"

@interface Analyzer ()
@property (nonatomic) NSMutableDictionary *entries;

@end

@implementation Analyzer

@synthesize entries = _entries;

- (void) analyzeContent:(NSString *)content
{
    // Lazy init
    if (!self.entries) self.entries = [NSMutableDictionary dictionary];
    
    // Clean
    [self.entries removeAllObjects];
    content = [content uppercaseString];
    
    // Temp dictionary
    NSMutableDictionary *tmp = [NSMutableDictionary dictionary];
    
    // Find mono-, di- and trigrams:
    for (int i = 0; i < content.length; i++) {
        for (int j = 1; j <= 3; j++) {
            if (i+j < content.length) {
                NSString *ch = [content substringWithRange:NSMakeRange(i, j)];
                BOOL valid = YES;
                for (int k = 0; k < j; k++) {
                    if ([ch characterAtIndex:k] < 'A' || [ch characterAtIndex:k] > 'Z') {
                        valid = NO;
                    }
                }
                if (valid) {
                    // Lazy init
                    if (![tmp objectForKey:ch]) {
                        [tmp setObject:[NSNumber numberWithInt:0] forKey:ch];
                    }
                    
                    // Increment counter
                    NSNumber *count = [tmp objectForKey:ch];
                    count = [NSNumber numberWithInt:[count intValue] + 1];
                    [tmp setObject:count forKey:ch];
                }
            }
        }
    }
    
    // Calculate and populate entries
    NSUInteger size = [[tmp allKeys] count];
    for (NSString* key in tmp) {
        NSNumber *count = [tmp objectForKey:key];
        Entry *entry = [[Entry alloc] initWithValue:key
                                      andOccurences:[count integerValue]
                                       andFrequency:[NSNumber numberWithFloat:[count floatValue]/(float)size]];
        [self.entries setObject:entry forKey:entry.value];
    }
    
}

@end
