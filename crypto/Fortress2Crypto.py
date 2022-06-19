from des import *
from datetime import datetime

class Fortress2Crypto:
    ChSeed = [
        0xD4, 0xCD, 0xA3, 0x1B, 0x61, 0x70, 0x41, 0xEE, 0x2A, 0xD6,
        0x6E, 0x04, 0x2E, 0xAF, 0xA3, 0x98, 0x68, 0xFF, 0xD8, 0xB6,
        0x26, 0x04, 0x7D, 0x3F, 0x68, 0x42, 0x26, 0xBC, 0xDC, 0xB7,
        0xB5, 0xD8, 0x22, 0x5D, 0xDA, 0x78, 0xD3, 0xD8, 0xB4, 0x7E,
        0x50, 0x84, 0xFE, 0x74, 0x58, 0xDF, 0x08, 0x6F, 0xF3, 0x20,
        0xC1, 0x5B, 0x62, 0x69, 0x70, 0x45, 0x26, 0xE0, 0x7A, 0x96,
        0xE3, 0x31, 0x3F, 0xFD, 0xC1, 0x01, 0x71, 0x40, 0x83, 0xDC,
        0x16, 0x83, 0x40, 0x42, 0x78, 0x44, 0xE8, 0x24, 0x85, 0x38,
        0x0D, 0x00, 0xF7, 0x51, 0xEE, 0xCB, 0x0A, 0x71, 0x25, 0xDB,
        0x48, 0xB9, 0xA5, 0x0E, 0x3E, 0xA3, 0x62, 0xBA, 0x35, 0xF8,
        0x31, 0x51, 0xBC, 0x74, 0xA7, 0x58, 0xA7, 0x1A, 0x8A, 0xBE,
        0xC4, 0x64, 0x46, 0x45, 0x3D, 0x6D, 0xDC, 0x61, 0x83, 0x4A,
        0xCC, 0x35, 0x15, 0x32, 0xF9, 0xCB, 0x06, 0xDD, 0x7F, 0x85,
        0xF3, 0xA9, 0x8C, 0x81, 0x27, 0x22, 0xB5, 0x51, 0x59, 0xB9,
        0x4C, 0x49, 0x2A, 0x3B, 0x5C, 0xBE, 0x0D, 0xAC, 0x26, 0x56,
        0x4B, 0xFD, 0x06, 0x9D, 0x66, 0xAD, 0xA0, 0xD7, 0x72, 0x09,
        0xD3, 0xDD, 0x58, 0x60, 0x35, 0xC6, 0x02, 0xE8, 0x78, 0x3C,
        0xC1, 0x43, 0x56, 0x75, 0x8A, 0xDC, 0xF0, 0x51, 0x65, 0x38,
        0xBB, 0x20, 0xC2, 0x69, 0xC5, 0x25, 0xAF, 0x12, 0x2D, 0x75,
        0x2C, 0x2A, 0x6B, 0xFA, 0x8B, 0xE2, 0x84, 0x27, 0xBD, 0x8E,
        0x39, 0x03, 0x5D, 0xDF, 0x13, 0x35, 0xCC, 0xDB, 0x25, 0x4C,
        0xCE, 0x0F, 0x1D, 0xD4, 0x17, 0x2C, 0xE4, 0xDF, 0xA1, 0x04,
        0xDC, 0x9E, 0xB2, 0xF5, 0x45, 0x47, 0x58, 0x4A, 0x2A, 0x92,
        0xF8, 0x42, 0x94, 0x8D, 0x72, 0xEB, 0x2B, 0xAA, 0x42, 0x6D,
        0x16, 0xC1, 0x45, 0x9B, 0xA9, 0x84, 0xF3, 0x78, 0x93, 0x63,
        0xEE, 0xDD, 0x47, 0x3A, 0x24, 0x65, 0x8A, 0x43, 0x97, 0x0D,
        0xF3, 0x7A, 0x93, 0x61, 0x25, 0xDA, 0xB5, 0x33, 0xC3, 0x68,
        0xF0, 0x09, 0x1F, 0xFA, 0xEE, 0x61, 0xF8, 0x59, 0x48, 0xF7,
        0x15, 0xEC, 0xF5, 0xD2, 0x20, 0x14, 0x3A, 0x5F, 0xCD, 0xC3,
        0x90, 0xF9, 0xC9, 0xBF, 0x92, 0xB8, 0x79, 0x22, 0x6C, 0x6D,
        0x4C, 0xC6, 0xC6, 0x17, 0x91, 0xDE, 0x68, 0x57, 0xBC, 0x27,
        0x6E, 0x99, 0x51, 0x0A, 0x9A, 0x98, 0xA5, 0xFB, 0xBC, 0xA9,
        0xDD, 0xEC, 0x7D, 0x5B, 0x9D, 0x17, 0x16, 0x53, 0xA0, 0xCE,
        0xA3, 0x99, 0x83, 0x03, 0x1B, 0x2D, 0x51, 0xD9, 0x7E, 0xA3,
        0xD6, 0x5F, 0x7F, 0x96, 0x48, 0xB1, 0xE9, 0x5B, 0x25, 0x82,
        0x50, 0x0C, 0x42, 0xEF, 0x00, 0x79, 0x88, 0x1A, 0xE8, 0x15,
        0x44, 0x16, 0x3D, 0x0E, 0x06, 0x48, 0x27, 0xA3, 0x67, 0xFF,
        0xFB, 0x6A, 0x5A, 0xE4, 0xA4, 0xF2, 0xE3, 0x51, 0x62, 0x68,
        0xFD, 0x56, 0x59, 0xD4, 0x07, 0xBA, 0x33, 0x90, 0x22, 0xA6,
        0x88, 0x4E, 0x9F, 0x38, 0x0C, 0xE0, 0x15, 0x5E, 0x06, 0x84,
        0xA2, 0xEA, 0xD3, 0xE1, 0x37, 0x69, 0x27, 0x1A, 0x2C, 0x38,
        0x8F, 0x2E, 0x01, 0xA4, 0x39, 0xE7, 0x60, 0xE7, 0x4B, 0xF0,
        0x22, 0xEF, 0xE6, 0xAB, 0xB3, 0x3B, 0xD9, 0xB6, 0x7C, 0xEA,
        0xC9, 0x1D, 0xC3, 0x5D, 0xE5, 0x5B, 0x8C, 0x02, 0x08, 0x4B,
        0xDB, 0x64, 0x6A, 0x26, 0x24, 0xB2, 0xE7, 0x53, 0x89, 0xB6,
        0x02, 0x64, 0xCA, 0xE4, 0x8D, 0xBA, 0x7B, 0x1C, 0x85, 0xA7,
        0xC6, 0x23, 0xB1, 0xC8, 0xF1, 0xAC, 0x3F, 0x9D, 0x12, 0x15,
        0xEC, 0x69, 0xE4, 0xD9, 0x7F, 0xC3, 0x67, 0xF9, 0x07, 0x7B,
        0x03, 0x15, 0x49, 0x85, 0x88, 0x30, 0xE0, 0xF8, 0xA5, 0xDB,
        0xD4, 0xA4, 0xDD, 0xA3, 0xC4, 0x3B, 0xCC, 0x08, 0x31, 0x22,
        0xA6, 0x66, 0xA4, 0xD3, 0xF0, 0x14, 0x7F, 0xD5, 0x1B, 0xC0,
        0x51, 0x85, 0x5D, 0x94, 0xD4, 0x85, 0xC8, 0x23, 0x79, 0x05,
        0xF8, 0xBD, 0x2A, 0xDF, 0x08, 0xAF, 0x20, 0xFC, 0x76, 0xB1,
        0x32, 0x84, 0xD6, 0x6F, 0x5E, 0xD7, 0x46, 0x59, 0x73, 0x14,
        0x47, 0x12, 0xB3, 0x8E, 0x17, 0xBE, 0xA6, 0x92, 0xC4, 0xDF,
        0x05, 0xCA, 0x83, 0x03, 0x98, 0x26, 0x07, 0xBF, 0x96, 0x68,
        0xE3, 0x09, 0xC0, 0xC7, 0xE3, 0xC2, 0xC1, 0x9B, 0x6D, 0x60,
        0xC8, 0xE7, 0x68, 0x4A, 0x0B, 0x6D, 0x73, 0x27, 0xB5, 0xBC,
        0x47, 0xF7, 0x73, 0xED, 0x10, 0x46, 0x62, 0x31, 0x0E, 0x35,
        0x5E, 0xE7, 0xFB, 0x35, 0x93, 0x3E, 0x0F, 0x7D, 0xD1, 0xE1,
        0x04, 0xC1, 0x9D, 0x00, 0xDD, 0x46, 0x62, 0x89, 0xD6, 0xEF,
        0x27, 0x87, 0x50, 0x16, 0xC1, 0xDA, 0x97, 0x68, 0x6D, 0xCA,
        0x9B, 0x76, 0x8D, 0x62, 0xF5, 0x29, 0xA2, 0x77, 0xC3, 0x3B,
        0x28, 0x63, 0xAE, 0x56, 0xBE, 0xAF, 0x39, 0x84, 0xDF, 0xF5,
        0xCD, 0x70, 0x18, 0xBD, 0x88, 0x8E, 0x33, 0xAB, 0xFE, 0x8A,
        0xD3, 0x97, 0xBB, 0xA1, 0x73, 0x28, 0xDD, 0x61, 0x77, 0xD7,
        0xDF, 0x18, 0x01, 0x8A, 0xEC, 0xE0, 0x36, 0xCA, 0x81, 0x62,
        0x09, 0x21, 0x40, 0x92, 0xB7, 0xCE, 0xD6, 0xAD, 0xE8, 0xCA,
        0xF1, 0x75, 0xF0, 0xC2, 0xDD, 0xE1, 0x9B, 0x19, 0xAD, 0xB9,
        0xE1, 0xE5, 0xDA, 0xB3, 0x3B, 0x60, 0x4D, 0x39, 0x77, 0x3D,
        0x62, 0xED, 0xBE, 0xEC, 0xA4, 0x87, 0xBD, 0x41, 0xA6, 0x88,
        0x8F, 0xF4, 0x38, 0x4C, 0x5C, 0x4F, 0xE3, 0x0B, 0x6A, 0xDE,
        0x49, 0xA5, 0x77, 0x65, 0x54, 0x87, 0x4C, 0x75, 0xB6, 0x93,
        0xE0, 0xAE, 0xD9, 0xFF, 0xE9, 0xD9, 0x67, 0x66, 0xF0, 0xEF,
        0x35, 0x21, 0x4F, 0xE2, 0x53, 0x87, 0x0B, 0xA0, 0xD8, 0x9B,
        0x29, 0x15, 0x75, 0x62, 0xD2, 0x8C, 0x68, 0xB6, 0x91, 0xEB,
        0x13, 0x38, 0x0C, 0xD7, 0x5C, 0x79, 0xCD, 0x85, 0x9E, 0x1B,
        0x3F, 0x94, 0x21, 0xFF, 0xB7, 0x02, 0x93, 0x09, 0xC4, 0x5A,
        0xFF, 0x16, 0xBC, 0x82, 0x69, 0xDD, 0xA7, 0x4E, 0xDB, 0x9A,
        0x9D, 0x75, 0xEB, 0xDD, 0x57, 0x23, 0xF0, 0x07, 0x8B, 0xC2,
        0x7A, 0x3B, 0x55, 0xBE, 0x0F, 0x07, 0xE2, 0x0A, 0x3D, 0x90,
        0x63, 0x55, 0x2B, 0xE9, 0x0E, 0xE3, 0xF2, 0x64, 0xA3, 0xCD,
        0x35, 0x7A, 0xF1, 0x8C, 0x9C, 0x1E, 0x31, 0xF6, 0x2A, 0xBD,
        0xAB, 0x4A, 0x49, 0xE9, 0x01, 0x61, 0xD7, 0x30, 0x47, 0x4D,
        0x5B, 0xA6, 0xE6, 0x88, 0x1F, 0xC1, 0x4F, 0xDA, 0xC7, 0xB3,
        0x17, 0x40, 0x69, 0xA8, 0xAE, 0x04, 0xF5, 0xED, 0x0C, 0x7D,
        0x74, 0xC4, 0xCA, 0x8F, 0x80, 0xF2, 0x62, 0x8B, 0x3E, 0x60,
        0x96, 0x3F, 0x6E, 0x85, 0x48, 0x73, 0xC0, 0xC2, 0x26, 0x1F,
        0x26, 0x6C, 0x48, 0x44, 0xB0, 0x52, 0xBD, 0x68, 0xDA, 0x37,
        0x7F, 0xFB, 0xF2, 0xF9, 0xE2, 0x35, 0xF0, 0xED, 0xF0, 0x88,
        0x6D, 0xE5, 0xD1, 0x5B, 0xEA, 0x66, 0xD2, 0xC9, 0x04, 0x3F,
        0xB2, 0xCB, 0x08, 0xC6, 0x7B, 0x86, 0xA7, 0x49, 0x30, 0xDA,
        0x2D, 0xFF, 0x0D, 0x56, 0x63, 0xEE, 0x66, 0xCC, 0xE8, 0x99,
        0x12, 0xE7, 0xB2, 0x32, 0x6B, 0xF1, 0x44, 0xFE, 0x62, 0xB7,
        0x8E, 0xDC, 0xFC, 0x6A, 0x1D, 0xE0, 0xC2, 0x57, 0x2B, 0x56,
        0xFB, 0x89, 0x19, 0x6A, 0xF2, 0xBE, 0xAC, 0xBD, 0xA5, 0x72,
        0x30, 0xDE, 0xC4, 0xC4, 0x06, 0xE2, 0xAD, 0xDD, 0x5D, 0xD5,
        0x79, 0xE6, 0x98, 0x80, 0x86, 0xC3, 0x69, 0x1A, 0xF1, 0x7C,
        0xE0, 0xB4, 0xAD, 0xCB, 0xCC, 0x83, 0xB4, 0xBD, 0x86, 0x55,
        0x56, 0xCE, 0x58, 0x52, 0x03, 0x7E, 0x60, 0x46, 0x17, 0x2F,
        0x32, 0xCA, 0x84, 0xB8, 0x83, 0xF2, 0x20, 0xFD, 0x6A, 0x95,
        0xA6, 0xFA, 0x5F, 0x13, 0xD5, 0x3E, 0x43, 0x6D, 0xCE, 0x5A,
        0x9A, 0xF5, 0x40, 0xE7, 0xD6, 0xB5, 0x94, 0x18, 0x6B, 0x73,
        0xA7, 0xD5, 0xA8, 0xF3, 0x33, 0xA9, 0x50, 0xD7, 0x9F, 0x9A,
        0x7D, 0x62, 0x27, 0xB7, 0x36, 0x30, 0x8D, 0x56, 0x3E, 0x5A,
        0x30, 0xD4, 0x90, 0xFC, 0x87, 0x1F, 0x41, 0x22, 0x95, 0xB4,
        0xD7, 0xF5, 0xC3, 0x38, 0x26, 0x9B, 0x69, 0x75, 0x10, 0x17,
        0xF9, 0x3C, 0x17, 0x50, 0x24, 0x6B, 0x3A, 0x2D, 0xCF, 0xE5,
        0x1A, 0xB3, 0x07, 0xF6, 0x23, 0xA7, 0xE3, 0x10, 0x3F, 0xF6,
        0xDB, 0x43, 0x9D, 0x0D, 0x25, 0xAD, 0x84, 0xB3, 0x63, 0x4E,
        0x3F, 0x18, 0xFD, 0x42, 0x3E, 0xEE, 0x1F, 0xD5, 0xE6, 0x68,
        0x50, 0xCB, 0x79, 0xA7, 0x75, 0x09, 0x77, 0x6C, 0xDB, 0x4A,
        0x41, 0x8B, 0xFB, 0xC3, 0x8C, 0x1A, 0x95, 0xD7, 0x2B, 0xD7,
        0xBF, 0xAB, 0x1C, 0x57, 0xF7, 0xF2, 0xA4, 0x48, 0x6E, 0x18,
        0x98, 0x9B, 0xAB, 0xFF, 0xCF, 0x4A, 0x6B, 0xD6, 0x99, 0x60,
        0x58, 0xB7, 0x47, 0xC5, 0x47, 0xB6, 0xC9, 0xEC, 0x92, 0x5A,
        0x3A, 0x65, 0xC9, 0x4D, 0x86, 0x92, 0x63, 0x61, 0xE6, 0xD6,
        0xAA, 0x33, 0x44, 0xE1, 0x44, 0x5B, 0x85, 0xB5, 0xF0, 0xEE,
        0x8A, 0xE2, 0x5A, 0x3C, 0xA9, 0xB5, 0xD2, 0x25, 0xBF, 0x0B,
        0x43, 0x0E, 0x4A, 0x27, 0xDB, 0xFA, 0xC7, 0x2E, 0xC4, 0x0C,
        0xED, 0x27, 0xB2, 0x72, 0xCA, 0xB1, 0x4D, 0x9D, 0x7F, 0x3F,
        0xA4, 0xEC, 0x62, 0x04, 0xCA, 0x18, 0x03, 0x64, 0xEC, 0xC3,
        0xB9, 0x74, 0x87, 0x48, 0xEF, 0xC1, 0xF5, 0x10, 0x36, 0x9B,
        0x44, 0xE7, 0xF8, 0x2F, 0xC9, 0x95, 0x79, 0xDC, 0xC2, 0x6A,
        0xB7, 0x9A, 0xBA, 0x5A, 0xC0, 0x84, 0xB3, 0x5C, 0xF8, 0x5B,
        0x05, 0x1B, 0x38, 0x08, 0x15, 0xD2, 0x8B, 0xC3, 0xF0, 0x9C,
        0xC9, 0x6A, 0xDD, 0x2A, 0x23, 0x6F, 0xD0, 0x05, 0x1B, 0x75,
        0xE2, 0xEE, 0x90, 0x65, 0x22, 0x4C, 0x75, 0xCB, 0x07, 0xBF,
        0x23, 0x38, 0x61, 0xB1, 0xCA, 0x4E, 0xD8, 0x22, 0xDE, 0x5C,
        0xBD, 0x67, 0x06, 0x72, 0x62, 0x33, 0x92, 0x5F, 0x6A, 0x4F,
        0xDF, 0x03, 0xBB, 0xD6, 0x4F, 0xCB, 0xA1, 0x57, 0xFB, 0x23,
        0x25, 0x9E, 0xF4, 0x8B, 0x01, 0x53, 0xD1, 0x5E, 0x38, 0xEC,
        0x50, 0xCD, 0xE1, 0x11, 0xF1, 0x29, 0xE1, 0x24, 0x93, 0x76,
        0x0D, 0x35, 0x9F, 0x4A, 0x4F, 0xA5, 0x0C, 0x75, 0x62, 0x5A,
        0x64, 0x46, 0xE3, 0xCA, 0x74, 0xB9, 0x71, 0xCF, 0x43, 0x31,
        0xF8, 0xD3, 0x4A, 0xDD, 0xAE, 0x90, 0x1B, 0x45, 0x5D, 0x03,
        0xDF, 0x16, 0xD3, 0xA0, 0x92, 0xCC, 0xB9, 0x78, 0x8A, 0x76,
        0x12, 0x54, 0x2D, 0x52, 0x9A, 0xF6, 0xD3, 0x91, 0x0E, 0x2A,
        0x85, 0xFE, 0x5F, 0x1E, 0x16, 0x42, 0xA1, 0x69, 0xF6, 0x56,
        0x42, 0x76, 0x64, 0xC9, 0xBB, 0x5C, 0xBB, 0x3A, 0x5A, 0x80,
        0x94, 0x95, 0xF6, 0x69, 0x25, 0x8C, 0x47, 0x0A, 0xB7, 0x15,
        0x00, 0x1A, 0xFC, 0xFF, 0x45, 0xB0, 0x3C, 0x05, 0x7E, 0x9E,
        0x12, 0x03, 0x20, 0xF8, 0xEC, 0x10, 0x36, 0x11, 0x8A, 0x9D,
        0xD3, 0x3A, 0xBE, 0xD5, 0x4C, 0x74, 0xE4, 0x1B, 0x1A, 0x8C,
        0x37, 0xFC, 0x97, 0x25, 0xC0, 0xB1, 0xA0, 0x1F, 0x97, 0x6A,
        0x36, 0x48, 0x87, 0x25, 0x04, 0x01, 0x77, 0x21, 0xEE, 0x12,
        0x77, 0x22, 0x0B, 0xDC, 0xDA, 0x5D, 0x39, 0x07, 0xBB, 0xD9,
        0xE4, 0xF2, 0x3F, 0xA1, 0xEC, 0x8D, 0x2C, 0x9E, 0xEE, 0x04,
        0x71, 0xF9, 0xAA, 0xA0, 0xDC, 0x5B, 0x04, 0x66, 0xDB, 0x96,
        0x7A, 0x93, 0xEF, 0x04, 0x8E, 0x59, 0x7C, 0xB0, 0x77, 0x00,
        0x57, 0x55, 0x48, 0x58, 0x09, 0xB7, 0x8C, 0x2A, 0x50, 0xF4,
        0xDE, 0xA1, 0xA7, 0x85, 0xEA, 0xA3, 0x83, 0xF0, 0x4C, 0xCB,
        0xD2, 0x7F, 0x0F, 0x4B, 0x33, 0xA5, 0x21, 0x8A, 0xB1, 0x91,
        0x67, 0x36, 0x9A, 0x05, 0x34, 0x7C, 0x71, 0xE9, 0x18, 0xB6,
        0x2D, 0x3D, 0x8A, 0xA2, 0xFB, 0x0B, 0x6B, 0xAC, 0x95, 0xE9,
        0x32, 0x2A, 0xA9, 0xC5, 0x52, 0xFA, 0x6E, 0x9F, 0xC4, 0x3A,
        0x1F, 0x64, 0x53, 0xE1, 0x77, 0x4C, 0xDC, 0x78, 0xB1, 0x31,
        0x64, 0x73, 0xE8, 0x81, 0x59, 0x4F, 0xE8, 0x5D, 0x49, 0x16,
        0x13, 0x40, 0xA3, 0xB9, 0x49, 0x6C, 0xC0, 0x07, 0x7A, 0x43,
        0x6D, 0xB3, 0x76, 0x98, 0x43, 0xAB, 0xF8, 0x12, 0x2E, 0xFE,
        0x1E, 0xA4, 0x63, 0x66, 0xA1, 0x6D, 0x60, 0x9F, 0xEC, 0x65,
        0xD8, 0xAA, 0x36, 0x23, 0xA0, 0xEF, 0xF8, 0x86, 0xE5, 0x52,
        0xCA, 0xA2, 0x07, 0xED, 0xDE, 0xA4, 0x6D, 0x7D, 0x2A, 0xE9,
        0x22, 0x74, 0x9E, 0x65, 0x55, 0xEB, 0x25, 0x72, 0xCD, 0xBF,
        0x5D, 0x66, 0xCC, 0xE2, 0x1A, 0x3E, 0x3C, 0x26, 0xF7, 0x4A,
        0x32, 0x11, 0x44, 0xF8, 0xFF, 0x52, 0xFC, 0x45, 0xC5, 0x39,
        0x88, 0x9B, 0x9B, 0x88, 0xC3, 0xCA, 0xD6, 0x24, 0x48, 0x8F,
        0x22, 0x4F, 0x8C, 0xD5, 0x38, 0xAB, 0xD5, 0x2B, 0x44, 0x08,
        0x67, 0xBD, 0x09, 0x60, 0x79, 0x96, 0xF6, 0xEE, 0x8C, 0x28,
        0x3D, 0xD6, 0x10, 0x81, 0xD6, 0x6D, 0x8E, 0xC8, 0xCB, 0xD5,
        0x63, 0x30, 0x09, 0x84, 0xA9, 0x31, 0x42, 0xCD, 0xD7, 0x98,
        0x40, 0xCD, 0xF9, 0x8E, 0x58, 0x54, 0xB6, 0x80, 0x35, 0x79,
        0x20, 0xDB, 0xE3, 0xC1, 0xF1, 0x6A, 0x5A, 0x00, 0x3F, 0xF0,
        0x62, 0x18, 0xA9, 0x8E, 0xFF, 0xA0, 0x49, 0xE2, 0x54, 0xE6,
        0xC8, 0xFD, 0x27, 0xC9, 0x96, 0x6B, 0x72, 0xA4, 0x3A, 0xC8,
        0x71, 0x57, 0xE5, 0xD7, 0x70, 0xAC, 0x20, 0x2B, 0xDD, 0xE6,
        0x3A, 0xF4, 0x15, 0x65, 0x97, 0x4C, 0x40, 0x22, 0x19, 0xA4,
        0x9C, 0x78, 0xB3, 0x70, 0x1A, 0x9E, 0xD7, 0x21, 0xD0, 0x5E,
        0x03, 0x32, 0xF9, 0x0E, 0xDE, 0xF8, 0x91, 0xDF, 0xBB, 0x55,
        0xEA, 0x71, 0x1B, 0x35, 0xA2, 0xB3, 0xB5, 0x2C, 0x0C, 0x9B,
        0xAC, 0x72, 0x0C, 0x3B, 0xA0, 0x77, 0x80, 0x5B, 0xAA, 0x32,
        0x42, 0xA1, 0x05, 0x6E, 0x86, 0xCE, 0x5F, 0x89, 0x4B, 0xA6,
        0x14, 0x65, 0xB4, 0x6C, 0x45, 0x83, 0x74, 0xFE, 0xB5, 0x4A,
        0x67, 0x75, 0x26, 0x40, 0x33, 0xC7, 0x2F, 0x75, 0xF2, 0x71,
        0xC4, 0xB4, 0x19, 0x88, 0x26, 0x99, 0x37, 0x05, 0xF7, 0x2A,
        0x94, 0x95, 0x85, 0x2E, 0x6E, 0x15, 0x3F, 0xE9, 0x2F, 0x11,
        0x66, 0x71, 0xEA, 0x2F, 0xEE, 0xE0, 0xAC, 0xB9, 0xB3, 0xF0,
        0x61, 0xAD, 0xF6, 0x11, 0xB8, 0xE6, 0x1A, 0xB1, 0x4C, 0x38,
        0x18, 0xA3, 0x3C, 0xD6, 0x1B, 0xB9, 0x0A, 0x07, 0x00, 0xA5,
        0xDC, 0x33, 0xB7, 0x7C, 0x44, 0x90, 0x1F, 0x83, 0x3E, 0xD5,
        0xA4, 0x57, 0x52, 0x23, 0x0C, 0x6D, 0x56, 0xBC, 0x8A, 0x50,
        0xD6, 0x5F, 0x15, 0xAC, 0x68, 0x38, 0x12, 0xA1, 0x20, 0xEE,
        0xF4, 0x8A, 0x02, 0x5B, 0x8C, 0x6B, 0x19, 0x96, 0x25, 0xFE,
        0x45, 0x99, 0x8B, 0x29, 0x8F, 0xC1, 0x42, 0xFE, 0x1A, 0xD8,
        0x64, 0xB0, 0xE3, 0xA1, 0x0B, 0x72, 0x55, 0x4A, 0xB2, 0xF3,
        0x9D, 0x7D, 0xF0, 0xB8, 0x75, 0xF4, 0xCF, 0x96, 0xC3, 0xD8,
        0x29, 0x7C, 0xFC, 0xAD, 0x4E, 0x04, 0x95, 0xC4, 0xC2, 0x36,
        0x37, 0x92, 0xEA, 0x11, 0x94, 0x93, 0x7A, 0x5D, 0xD7, 0x69,
        0x04, 0x39, 0xBE, 0x87, 0x0D, 0xCE, 0xBB, 0x20, 0x08, 0xAD,
        0x68, 0xE0, 0xDE, 0x8B, 0xB9, 0x39, 0xA0, 0x31, 0xDB, 0xF7,
        0x3A, 0x6B, 0xC0, 0xF3, 0xD5, 0x41, 0xBD, 0x92, 0xA5, 0x7A,
        0x97, 0x06, 0x0F, 0x4B, 0x97, 0x94, 0x6B, 0x7A, 0x7E, 0x26,
        0x45, 0x97, 0x97, 0x05, 0x78, 0x18, 0xFF, 0xCA, 0xE4, 0xD3,
        0xD0, 0x53, 0x07, 0xF2, 0x35, 0xDF, 0x53, 0x78, 0x1E, 0x96,
        0x06, 0x2F, 0xCD, 0xC3, 0xBB, 0x3C, 0x40, 0x3B, 0xF0, 0xCC,
        0xD8, 0xF8, 0x7D, 0x4B, 0x73, 0xAE, 0x48, 0xE2, 0xC7, 0x6A,
        0x06, 0xF5, 0x2E, 0xDD, 0x0B, 0xD0, 0xB2, 0x70, 0x57, 0xEC,
        0x9D, 0x11, 0xF0, 0x5C, 0x5B, 0xA2, 0x3C, 0x27, 0x96, 0xBB,
        0x5E, 0x9F, 0x32, 0x7A, 0x3B, 0x7F, 0x90, 0xAE, 0x60, 0xD0,
        0xE8, 0xDC, 0x29, 0x20, 0x0C, 0x5E, 0xD2, 0xD5, 0x84, 0xC8,
        0x10, 0x8B, 0x88, 0xAF, 0xD7, 0xD2, 0x6B, 0x9A, 0xEE, 0x9D,
        0x17, 0xB9, 0x88, 0x62, 0x8E, 0x4F, 0x34, 0xA3, 0x3E, 0x4F,
        0x96, 0x22, 0x92, 0x94, 0x50, 0x25, 0x24, 0x0A, 0x6D, 0x09,
        0x1A, 0x6A, 0xB1, 0xE2, 0x3F, 0xB6, 0x1C, 0xB2, 0xE6, 0x1D,
        0x4B, 0xF0, 0x21, 0x72, 0xB4, 0x10, 0x78, 0x0A, 0xC0, 0x91,
        0x16, 0xDA, 0x12, 0xB1, 0xF0, 0x77, 0x01, 0x64, 0xE3, 0xBE,
        0x5A, 0x1E, 0xA9, 0x09, 0x10, 0xBA, 0xF1, 0x89, 0xEC, 0xBE,
        0x99, 0xCF, 0xC9, 0x96, 0xA5, 0xA2, 0x88, 0xBF, 0x91, 0x97,
        0xAF, 0x30, 0xD1, 0x54, 0x0F, 0xFD, 0x7F, 0xC7, 0x7F, 0x08,
        0x07, 0x98, 0x04, 0xBF, 0x53, 0xAB, 0x9D, 0xEC, 0xB7, 0x6C,
        0x69, 0x7B, 0x91, 0x53, 0x06, 0x63, 0x8C, 0x0C, 0xA1, 0xA0,
        0xE1, 0xFB, 0x0E, 0x89, 0xB7, 0xE2, 0x19, 0x8C, 0xB5, 0x12,
        0xA8, 0x7B, 0x65, 0x77, 0xD9, 0x5D, 0x42, 0x2E, 0x51, 0x22,
        0x4C, 0x84, 0x88, 0x75, 0xAA, 0xC4, 0x5C, 0xF1, 0x58, 0x67,
        0x27, 0xEE, 0x8D, 0xD9, 0xF9, 0x30, 0xC7, 0x78, 0xED, 0x5E,
        0x91, 0x02, 0xB4, 0x46, 0x37, 0xA9, 0xC0, 0x7E, 0xAB, 0xB9,
        0xB8, 0x8B, 0x8D, 0xEA, 0x8A, 0xE1, 0x91, 0x82, 0xAD, 0x34,
        0x6E, 0xE8, 0x49, 0xB0, 0x3A, 0x07, 0x7A, 0xF7, 0xE3, 0x72,
        0x3C, 0x58, 0x1A, 0x67, 0xAC, 0xE0, 0x17, 0x56, 0xFE, 0x6E,
        0x3D, 0x9A, 0xD8, 0xEA, 0x84, 0x09, 0x86, 0x59, 0x1A, 0x8E,
        0x2E, 0x3C, 0x62, 0xE4, 0xA2, 0x9E, 0x09, 0x1D, 0xE7, 0x24,
        0x68, 0x8B, 0xDD, 0x05, 0x09, 0xA0, 0x1F, 0xF0, 0xBE, 0x57,
        0x55, 0x2B, 0xB2, 0x38, 0x81, 0x5E, 0xCE, 0xFB, 0x29, 0x2F,
        0x9A, 0x1E, 0x79, 0x71, 0x78, 0xF4, 0x73, 0xCD, 0x2C, 0xB2,
        0xF5, 0xCF, 0xF4, 0x80, 0x57, 0xBA, 0xF8, 0xF1, 0x9F, 0x00,
        0x61, 0x90, 0xFB, 0x63, 0xAE, 0x44, 0x45, 0x08, 0x82, 0xF8,
        0x40, 0xFA, 0x07, 0x5D, 0x19, 0x8B, 0xEF, 0xDF, 0xB8, 0xFD,
        0x29, 0x02, 0x35, 0xB6, 0x19, 0x90, 0xEF, 0x5F, 0xCD, 0xC2,
        0xD1, 0xEA, 0xBB, 0x33, 0xE7, 0x2A, 0x4F, 0xA8, 0x4A, 0xEE,
        0x9C, 0x78, 0x47, 0x6B, 0xA5, 0x8F, 0xBE, 0xB5, 0x12, 0x1F,
        0xA9, 0x77, 0x1D, 0x25, 0x5D, 0x75, 0x5C, 0x10, 0xAB, 0x2A,
        0xFF, 0x17, 0x05, 0xD3, 0xC1, 0x8A, 0x35, 0x9E, 0x23, 0x87,
        0xA1, 0x91, 0xC5, 0x67, 0xB3, 0x13, 0x3E, 0x2F, 0xC2, 0x10,
        0xD2, 0x44, 0xB0, 0xDA, 0x33, 0xA6, 0x3E, 0xC7, 0xE9, 0x3E,
        0x34, 0x04, 0xD0, 0xA4, 0xF5, 0x5B, 0x6A, 0xCF, 0x92, 0x61,
        0xA4, 0x15, 0xE3, 0xE5, 0x71, 0x70, 0x2A, 0x58, 0xAF, 0xA4,
        0xCC, 0x70, 0x83, 0x29, 0x71, 0xD1, 0xBD, 0x61, 0x89, 0xD2,
        0x47, 0xC4, 0x57, 0x24, 0xD5, 0xB7, 0x76, 0x47, 0x15, 0x63,
        0x00, 0xCC, 0x8C, 0x9F, 0x74, 0xB4, 0xAB, 0xF0, 0xF6, 0x65,
        0x4C, 0x4F, 0x1E, 0x32, 0x4B, 0x1B, 0x8B, 0x84, 0x04, 0x38,
        0xC0, 0x06, 0x4E, 0x01, 0x42, 0x07, 0xD1, 0x9D, 0xA7, 0xA1,
        0x61, 0xB4, 0x03, 0xF5, 0xC3, 0x40, 0xB9, 0x52, 0xAF, 0xFA,
        0x3C, 0x7F, 0x6E, 0xC6, 0x4B, 0x3D, 0x1C, 0xC4, 0x3C, 0x9B,
        0xEE, 0x16, 0xDB, 0x6F, 0xA6, 0xF9, 0xBA, 0xDF, 0xE7, 0x89,
        0xAD, 0x5C, 0x4D, 0xA3, 0x28, 0xAC, 0x46, 0x6B, 0x81, 0xD5,
        0x6C, 0x42, 0xB6, 0x6E, 0xBD, 0xD3, 0xED, 0x15, 0x9A, 0x29,
        0x5C, 0xF2, 0xF3, 0xB3, 0x92, 0xD0, 0x77, 0xE2, 0x7A, 0x3C,
        0xAD, 0x9E, 0x29, 0x8B, 0x6C, 0xAB, 0xBF, 0xFF, 0x25, 0x99,
        0x1C, 0x3D, 0xDB, 0x84, 0x86, 0x6C, 0xD0, 0xCA, 0x83, 0x5F,
        0xF5, 0x06, 0x65, 0x3A, 0x20, 0xC2, 0xD4, 0x9C, 0xA5, 0x40,
        0xD0, 0xB5, 0x39, 0x31, 0x98, 0x28, 0xEA, 0x5A, 0x79, 0xC5,
        0x5C, 0x8D, 0x97, 0x6F, 0xC8, 0x49, 0xC7, 0xAB, 0x81, 0x75,
        0x48, 0x39, 0x91, 0xB6, 0x90, 0x6D, 0xB3, 0x29, 0x14, 0x90,
        0x90, 0xAD, 0x1B, 0xEF, 0x10, 0x13, 0xFD, 0xAD, 0x78, 0xF8,
        0xF3, 0x1C, 0x1C, 0x8C, 0x9D, 0x3D, 0xE9, 0x89, 0xA6, 0x2D,
        0x8A, 0x21, 0x84, 0xAC, 0x54, 0xF8, 0xB6, 0x26, 0xE1, 0xA6,
        0x81, 0x9F, 0x64, 0xA0, 0xD9, 0x9D, 0x77, 0x13, 0x52, 0x67,
        0xFF, 0xB8, 0xF2, 0x26, 0xB2, 0x2B, 0xA8, 0x84, 0xFB, 0x38,
        0x50, 0x12, 0x08, 0xF2, 0x5E, 0xB8, 0x51, 0xA4, 0x43, 0xFD,
        0xA4, 0xF1, 0x35, 0x5D, 0x91, 0x56, 0x5E, 0x94, 0xE4, 0xF0,
        0x18, 0xF2, 0x7E, 0x75, 0x52, 0xCC, 0x7E, 0x1F, 0xC9, 0x7D,
        0xB1, 0xA9, 0x10, 0xC9, 0x6A, 0x57, 0xCE, 0x4A, 0xCE, 0x89,
        0x4F, 0x2D, 0x52, 0x63, 0x87, 0xF8, 0x77, 0xD9, 0xAD, 0x2D,
        0x4A, 0x23, 0x62, 0x15, 0x99, 0xB2, 0x07, 0xD3, 0x21, 0x11,
        0xCF, 0x23, 0x4C, 0x7A, 0x39, 0x4A, 0x27, 0x22, 0x63, 0x79,
        0x6C, 0x0A, 0x4A, 0xDD, 0xCA, 0x5C, 0x02, 0x86, 0x55, 0x54,
        0xA2, 0xC9, 0x6C, 0x8D, 0xDE, 0x45, 0xD3, 0xB6, 0x05, 0x59,
        0x44, 0x6A, 0xD2, 0x92, 0xEF, 0x0C, 0x7F, 0xE7, 0x88, 0x80,
        0x4A, 0xF6, 0xE7, 0xBF, 0x84, 0xD8, 0x67, 0xD7, 0xC9, 0x4B,
        0xE7, 0x61, 0xB0, 0x41, 0x19, 0x77, 0x9E, 0xEC, 0x76, 0x3E,
        0x0C, 0x1B, 0x7C, 0xB9, 0x72, 0x81, 0x70, 0xBB, 0x0C, 0x81,
        0x8E, 0xF2, 0x56, 0x92, 0x8B, 0x75, 0xB0, 0xBC, 0x1D, 0xA7,
        0xE1, 0x53, 0xA6, 0x97, 0x94, 0x24, 0xA2, 0x54, 0x90, 0x5D,
        0x0B, 0x43, 0x33, 0x49, 0xEA, 0x59, 0xAD, 0xC6, 0xAD, 0x00,
        0x94, 0xC3, 0xC5, 0xA0, 0x7A, 0xC5, 0x31, 0x5B, 0x56, 0x69,
        0xFD, 0x93, 0x26, 0xDD, 0xA5, 0xB9, 0x89, 0x77, 0x77, 0xD7,
        0x15, 0xF4, 0x05, 0xDA, 0xB7, 0x90, 0x2D, 0xE4, 0x75, 0x3F,
        0x8A, 0x9C, 0x3A, 0x18, 0x26, 0xFA, 0xB8, 0xA0, 0x84, 0xF8,
        0xD4, 0xB5, 0x94, 0x41, 0xAE, 0x54, 0xFB, 0xE6, 0xFA, 0x7A,
        0xB3, 0x67, 0x63, 0x02, 0xAC, 0x88, 0x65, 0x31, 0xA5, 0x32,
        0x23, 0xFB, 0x60, 0x20, 0x1B, 0xA6, 0x72, 0x7E, 0xDE, 0x35,
        0xA9, 0x55, 0x56, 0x63, 0x79, 0x20, 0x52, 0x84, 0xCC, 0xE5,
        0x48, 0x3B, 0xED, 0x0C, 0x83, 0x20, 0x55, 0xDF, 0xE8, 0x71,
        0x05, 0x56, 0xDA, 0x6B, 0x26, 0xE8, 0x5A, 0xA1, 0x39, 0x13,
        0xC7, 0x2E, 0xCD, 0x53, 0xA3, 0x47, 0xA1, 0xE2, 0x40, 0x2D,
        0x11, 0xF4, 0x8F, 0xEA, 0xA6, 0x62, 0x49, 0x39, 0x5C, 0x8F,
        0x8F, 0xDD, 0x42, 0x8D, 0x57, 0x6B, 0x9A, 0x47, 0x89, 0xA2,
        0xCE, 0xD5, 0xF0, 0xC4, 0x25, 0x52, 0xD7, 0x72, 0x74, 0x6D,
        0xB2, 0x66, 0x9F, 0x91, 0xF7, 0xBA, 0x2C, 0xF5, 0x47, 0x1B,
        0x40, 0xE0, 0xE2, 0xD6, 0x92, 0x0D, 0xE9, 0x57, 0xE4, 0x39,
        0x8B, 0x6A, 0x92, 0x1C, 0x5B, 0x2A, 0xDD, 0xCC, 0x36, 0xDC,
        0x41, 0x43, 0x1F, 0x93, 0xF9, 0x77, 0x37, 0xFA, 0x28, 0x23,
        0x86, 0xC9, 0x19, 0xFB, 0xB4, 0x73, 0xD2, 0xAF, 0x1D, 0xFB,
        0xE3, 0x94, 0x43, 0x87, 0xBB, 0xEA, 0x9E, 0x1A, 0x55, 0xAA,
        0xE5, 0x27, 0xCF, 0xA5, 0x81, 0x0A, 0x68, 0x77, 0x3E, 0x0A,
        0x27, 0x24, 0xA9, 0x98, 0xB6, 0xC9, 0x09, 0x5F, 0x4F, 0x86,
        0xD1, 0xD0, 0x40, 0xA1, 0x43, 0xD8, 0x2E, 0x5C, 0x82, 0x27,
        0x73, 0x21, 0xF1, 0x8D, 0x48, 0x6C, 0x98, 0xD0, 0x86, 0x63,
        0xD3, 0x74, 0x7B, 0xE4, 0xDF, 0x4C, 0x7B, 0x81, 0x69, 0xA3,
        0xB9, 0x4E, 0x50, 0x2B, 0x15, 0xAF, 0x66, 0xC8, 0x3D, 0xED,
        0x8E, 0x6B, 0x49, 0x5A, 0xD9, 0xF5, 0x92, 0xC3, 0xC3, 0x9C,
        0x54, 0xED, 0xAD, 0x55, 0x8D, 0x5E, 0x88, 0xCD, 0x4D, 0xAC,
        0xE5, 0xE7, 0xA1, 0x9D, 0x79, 0xBE, 0xE4, 0x12, 0x10, 0xC6,
        0x88, 0xE2, 0xB6, 0x86, 0x5F, 0x75, 0x63, 0x2B, 0x21, 0x0B,
        0xD0, 0x15, 0xA4, 0xF8, 0xEF, 0xEF, 0xF2, 0x85, 0x07, 0xC2,
        0x7D, 0x59, 0xEE, 0x38, 0x0D, 0xC4, 0x95, 0xA8, 0x7E, 0x3B,
        0xBA, 0xD9, 0xCD, 0x11, 0x00, 0x85, 0xF2, 0xDD, 0xC1, 0xC4,
        0x91, 0x08, 0xCE, 0x99, 0x65, 0x1C, 0xD8, 0x3A, 0xFF, 0x91,
        0x35, 0x66, 0x40, 0x27, 0xA5, 0x87, 0xCC, 0x3F, 0x1A, 0x11,
        0x6F, 0x98, 0xBA, 0x59, 0x16, 0x9F, 0xC2, 0x12, 0x9D, 0x9D,
        0xFD, 0x6D, 0xBF, 0xFB, 0xF5, 0x0D, 0xC0, 0xF7, 0x9D, 0x8D,
        0x95, 0xDA, 0xA6, 0x39, 0xEC, 0x95, 0x07, 0x73, 0xB9, 0x4E,
        0x55, 0xD1, 0x3E, 0xA9, 0xFC, 0xD0, 0x40, 0x51, 0x99, 0xE6,
        0xA2, 0x8D, 0x4F, 0xA9, 0xA8, 0x1D, 0x76, 0x9B, 0x69, 0xBB,
        0xC9, 0x4D, 0xD1, 0x3B, 0x0E, 0x81, 0xAC, 0x20, 0x79, 0xA1,
        0x07, 0xFB, 0xC8, 0x52, 0x3D, 0x81, 0x6F, 0xC4, 0xF8, 0x45,
        0x9B, 0x0E, 0x1C, 0xF6, 0xB3, 0x57, 0x00, 0xB4, 0x3E, 0x2D,
        0xFA, 0x5F, 0x28, 0x4B, 0x41, 0xB9, 0xFF, 0xBA, 0x28, 0x79,
        0xEF, 0x7C, 0x5C, 0x3C, 0x1E, 0xB1, 0xA7, 0xE0, 0x3B, 0xCA,
        0xCC, 0x81, 0x2E, 0x9C, 0x2C, 0x0E, 0xBF, 0x87, 0xD3, 0xA0,
        0xCE, 0xC5, 0x7D, 0xF2, 0xC0, 0x5E, 0xFC, 0xE9, 0xB5, 0xD8,
        0x2F, 0x26, 0x01, 0xBC, 0xF7, 0x89, 0xA1, 0x1B, 0xA4, 0x82,
        0x3D, 0x10, 0xF3, 0x21, 0x20, 0xB8, 0xD8, 0x8F, 0x97, 0x04,
        0xDA, 0x10, 0x53, 0xC2, 0xFA, 0x63, 0xFB, 0x6E, 0xFE, 0x42,
        0x05, 0xE8, 0x31, 0x83, 0x09, 0x9F, 0xEF, 0xB9, 0x15, 0xFD,
        0x76, 0x4E, 0x97, 0x2E, 0xCB, 0x02, 0xE7, 0x1A, 0x82, 0xB9,
        0xED, 0x09, 0xBC, 0xD4, 0xC3, 0xA0, 0x84, 0xD7, 0xF7, 0x3C,
        0x4B, 0x8D, 0x67, 0xF8, 0x99, 0x47, 0x01, 0x27, 0x87, 0x3B,
        0xF2, 0x26, 0x91, 0x20, 0x0C, 0x42, 0x39, 0xDE, 0x50, 0xCA,
        0xE0, 0x62, 0xEB, 0x7E, 0xFE, 0xFE, 0x6A, 0xC4, 0x66, 0x4A,
        0xD7, 0x79, 0x8A, 0x7D, 0xCA, 0x14, 0x47, 0xA2, 0x40, 0xE3,
        0x99, 0x80, 0x61, 0x32, 0x25, 0xCA, 0xC9, 0xFE, 0x84, 0x2F,
        0xCA, 0x0A, 0xB8, 0xF6, 0xDC, 0x71, 0xE6, 0x17, 0xE1, 0xAD,
        0x68, 0x36, 0xC8, 0xF1, 0x85, 0xD2, 0xC7, 0x4C, 0xFE, 0x3A,
        0xF9, 0xFB, 0x89, 0x77, 0xB6, 0x0D, 0xD9, 0x60, 0xC8, 0xDE,
        0x5C, 0x17, 0x77, 0x7A, 0x54, 0xBB, 0x56, 0x09, 0x70, 0x39,
        0xD6, 0x25, 0x02, 0xCA, 0x50, 0x98, 0x51, 0x44, 0x70, 0x22,
        0x4D, 0x5F, 0x1E, 0xB8, 0x60, 0x63, 0x6A, 0xC8, 0x63, 0xDC,
        0x91, 0x44, 0x89, 0x98, 0x0F, 0x2D, 0xC7, 0xA7, 0x43, 0x07,
        0x9D, 0xEC, 0x75, 0x73, 0x24, 0x4C, 0x99, 0xEB, 0xC1, 0x53,
        0xB8, 0xF6, 0xF1, 0xFF, 0x7D, 0x6B, 0xCC, 0xCF, 0x82, 0xE6,
        0xD0, 0x04, 0xD4, 0xC4, 0xDB, 0x0D, 0x0C, 0x4B, 0x70, 0xBD,
        0x5A, 0x8C, 0x9F, 0x39, 0xD0, 0x6A, 0x42, 0x4D, 0x3A, 0xC5,
        0xBD, 0x14, 0x90, 0x28, 0x9E, 0x11, 0x79, 0xC5, 0xC8, 0xE3,
        0x7C, 0x07, 0x3D, 0xFF, 0x79, 0x7B, 0x44, 0xC0, 0x06, 0x34,
        0x68, 0x8B, 0xA3, 0x3A, 0xCF, 0x7E, 0x68, 0x35, 0x2B, 0x90,
        0x51, 0xE2, 0xC8, 0x63, 0xDC, 0xED, 0x1D, 0x5A, 0x47, 0x02,
        0x89, 0x91, 0xF2, 0xF5, 0xCA, 0x91, 0x3B, 0x02, 0x5A, 0x55,
        0xB9, 0xF0, 0xB7, 0xA1, 0x1A, 0xA8, 0x9C, 0xF5, 0xE5, 0x7E,
        0x7E, 0x64, 0x6C, 0xD3, 0x53, 0xF6, 0xD0, 0xD0, 0xE0, 0xBE,
        0x06, 0xED, 0x05, 0x4A, 0x7C, 0xF1, 0xE1, 0x7E, 0xF4, 0xCA,
        0xE8, 0xB8, 0x96, 0xD3, 0x3B, 0xAD, 0x51, 0x3C, 0x09, 0x7C,
        0xAE, 0xD7, 0xA4, 0x64, 0xB4, 0xC6, 0x33, 0x86, 0x26, 0xB1,
        0xB8, 0x9B, 0xAE, 0x7B, 0x5B, 0x7A, 0x1D, 0xAD, 0xB2, 0x16,
        0x3B, 0x50, 0x67, 0x25, 0xF6, 0x7F, 0x49, 0x50, 0xB0, 0x1A,
        0x6C, 0x96, 0xA7, 0x3E, 0xE1, 0xCB, 0x0B, 0x5B, 0xE5, 0x91,
        0xB1, 0x27, 0x5B, 0x6A, 0xA5, 0x9D, 0x7C, 0x05, 0xD3, 0x0C,
        0xC7, 0x3A, 0x16, 0x6B, 0x80, 0xC3, 0x98, 0x68, 0x79, 0x1A,
        0xB2, 0xBD, 0xD5, 0xC0, 0xF5, 0xA7, 0xF7, 0xF1, 0x81, 0x13,
        0xE1, 0xF5, 0xA5, 0x87, 0xB6, 0xA1, 0x04, 0xB4, 0xF5, 0xB8,
        0x91, 0x27, 0xC4, 0x10, 0x34, 0xB0, 0x51, 0x90, 0x68, 0x70,
        0x2C, 0xA9, 0x88, 0x1D, 0x12, 0xBD, 0xAE, 0x50, 0x4D, 0xD0,
        0x22, 0xBE, 0xD0, 0x81, 0xD9, 0x30, 0x41, 0x12, 0xF7, 0xE6,
        0x52, 0xF1, 0xC2, 0x50, 0x0E, 0x74, 0x8A, 0xA5, 0x7A, 0x12,
        0xC0, 0xE6, 0xA6, 0x35, 0x25, 0xB8, 0x0E, 0x49, 0x42, 0x73,
        0x64, 0x1A, 0x8B, 0xEF, 0xE0, 0x2B, 0x5F, 0x1C, 0x6C, 0xBF,
        0xFE, 0x34, 0x13, 0xB6, 0xD8, 0xB7, 0x6A, 0xF8, 0xFA, 0x27,
        0xD0, 0x21, 0x1F, 0x25, 0xE7, 0xAA, 0xF8, 0xB9, 0xBD, 0x76,
        0xC2, 0xCB, 0x0C, 0xC7, 0xF7, 0xC4, 0xD1, 0xEF, 0x38, 0xF8,
        0xD4, 0x7D, 0x48, 0x45, 0xD4, 0x44, 0xD8, 0x11, 0x68, 0x0A,
        0x77, 0xDB, 0xC4, 0x6A, 0x2A, 0xAD, 0x46, 0x8C, 0xCD, 0xAF,
        0x01, 0xCC, 0x60, 0xB6, 0x3B, 0x64, 0x05, 0xC4, 0x9A, 0x4A,
        0x1B, 0x72, 0xCE, 0x9A, 0xF0, 0x5B, 0x78, 0x24, 0xF7, 0x87,
        0xDF, 0x46, 0x1B, 0x23, 0x34, 0x18, 0xDF, 0x56, 0x6D, 0x67,
        0xE6, 0x18, 0x27, 0x0C, 0x24, 0x7A, 0x06, 0x28, 0x7F, 0xDE,
        0x69, 0xC6, 0x6D, 0x7C, 0xCD, 0xD2, 0x8A, 0x26, 0xC9, 0x35,
        0xF3, 0x3F, 0xBE, 0xA8, 0x6E, 0xD4, 0x6C, 0x51, 0x74, 0xB6,
        0x5B, 0x0F, 0x33, 0xE0, 0x4B, 0x4D, 0x48, 0x5D, 0xED, 0xE6,
        0xCA, 0x88, 0xE7, 0x9D, 0xAD, 0xE5, 0x4C, 0x10, 0x4C, 0x40,
        0x1C, 0x48, 0xF6, 0x81, 0xD6, 0x9C, 0xE3, 0x08, 0xE6, 0x37,
        0xB4, 0x2D, 0x55, 0x10, 0x5B, 0x1F, 0xBB, 0xBB, 0x89, 0x68,
        0x40, 0xC2, 0x84, 0x0A, 0xC0, 0x4D, 0xAE, 0x49, 0xA6, 0x78,
        0xC8, 0x81, 0x8C, 0xFF, 0x12, 0x7D, 0xE9, 0xA5, 0x78, 0x24,
        0xEF, 0x31, 0x1A, 0x95, 0x99, 0x0A, 0x8F, 0x0F, 0x89, 0x83,
        0x6D, 0xEA, 0x8A, 0xDC, 0xAC, 0x05, 0x4C, 0xD9, 0x7C, 0xAC,
        0xE1, 0x93, 0x33, 0x62, 0x25, 0x5F, 0x01, 0xC3, 0x4D, 0x67,
        0xC2, 0x67, 0x22, 0x11, 0xD3, 0xC5, 0xD1, 0xA0, 0xDE, 0x6E,
        0xCE, 0xBA, 0x3A, 0x9E, 0xBD, 0xA6, 0xE0, 0xF6, 0x4A, 0x25,
        0x69, 0xAA, 0xB6, 0x3B, 0xC1, 0x17, 0x69, 0x58, 0xD3, 0x02,
        0x3B, 0x34, 0x5C, 0x5C, 0x88, 0xF9, 0xD3, 0x6D, 0x4A, 0xD8,
        0x6A, 0x97, 0x6A, 0x7F, 0xD8, 0x12, 0x0D, 0x17, 0xF4, 0x6A,
        0xD4, 0x24, 0x6B, 0xF6, 0xB5, 0xCF, 0x36, 0xE2, 0x38, 0x04,
        0xB7, 0x34, 0x56, 0x46, 0xC1, 0x80, 0x4D, 0x2B, 0xE6, 0x01,
        0x99, 0x0D, 0x63, 0x23, 0x04, 0x37, 0xC7, 0x6A, 0x3A, 0x76,
        0x71, 0x7A, 0x98, 0x64, 0xD9, 0xC7, 0xAC, 0x01, 0x63, 0xB8,
        0x5E, 0x28, 0xBE, 0x3A, 0xF4, 0x09, 0x1F, 0xF0, 0x9E, 0xDA,
        0x02, 0xBD, 0xF8, 0xF0, 0x19, 0xBB, 0xD1, 0x67, 0xCE, 0x1C,
        0x5A, 0xEF, 0xAC, 0x80, 0x9C, 0x41, 0x32, 0x54, 0x1E, 0x5C,
        0x3B, 0xFC, 0xCE, 0xC1, 0x22, 0xD6, 0x32, 0x88, 0xC1, 0xFD,
        0xF6, 0x91, 0x4D, 0xE7, 0x96, 0x2F
    ]
    def __init__(self):
        self.this_4 = 0
        self.this_5 = 0
        self.this_6 = 0
        self.this_7 = 0
        self.this_8 = 0

        # Set seed by time?? wtf..
        time = datetime.now()
        miliseconds = time.microsecond
        seconds = time.second
        minutes = time.minute
        self.SetSeed(
            (miliseconds + (100 * seconds) + (112 * minutes)) & 0xFF
        )
        return

    def CalcMD5(self):
        return
    
    def SetSeed(self, seed: int):
        # Seed should be char range
        assert seed <= 0xFF
        self.this_4 = seed
        self.this_5 = seed
        self.this_6 = seed
        self.this_7 = seed
        self.this_8 = seed

    def ServerDecode(self, a2, a4):
        # a3 = output
        a3 = []
        setkey(0, 1, self.ChSeed[16 * (self.this_4)])
        i = 0
        while i < (a4 % 8 != 0) + (a4//8):
            a3.append(a2[8*i:8*(i+1)])
            i += 1
        return a3