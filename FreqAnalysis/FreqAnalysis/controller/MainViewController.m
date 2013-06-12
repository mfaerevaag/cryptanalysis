//
//  MainViewController.m
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import "MainViewController.h"
#import "Analyzer.h"

#define CYPHERTEXT_FILE @"Text"

@interface MainViewController ()
@property (copy) NSString *text;
@property Analyzer *analyzer;


@end

@implementation MainViewController

@synthesize analyzer = _analyzer,
text = _text;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        _analyzer = [[Analyzer alloc] init];
    }
    
    return self;
}

- (IBAction)analyze:(id)sender
{
    if (!self.text) {
        NSString *path = [[NSBundle mainBundle] pathForResource:CYPHERTEXT_FILE
                                                         ofType:@"txt"];
        self.text = [NSString stringWithContentsOfFile:path
                                              encoding:NSUTF8StringEncoding
                                                 error:NULL];
    }
    
    [self.analyzer analyzeContent:self.text];
}

@end
